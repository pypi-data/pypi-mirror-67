#define PY_SSIZE_T_CLEAN

#include <math.h>
#include <Python.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include "hll.h"
#include "structmember.h"
#include "../lib/murmur3.h"

typedef struct {
    PyObject_HEAD
    char * registers; /* contains the ranks */
    uint32_t seed;    /* Murmur3 seed */
    uint32_t size;    /* number of registers */
    unsigned short k; /* size = 2^k */
    double cache;     /* cache of cardinality estimate */
    bool use_cache;   /* use cached cardinality */
} HyperLogLog;

static void
HyperLogLog_dealloc(HyperLogLog* self)
{
    free(self->registers);
    #if PY_MAJOR_VERSION >= 3
        Py_TYPE(self)->tp_free((PyObject*) self);
    #else
        self->ob_type->tp_free((PyObject*) self);
    #endif
}

static PyObject *
HyperLogLog_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    HyperLogLog *self;
    self = (HyperLogLog *)type->tp_alloc(type, 0);
    self->seed = 314;
    return (PyObject *)self;
}

static int
HyperLogLog_init(HyperLogLog *self, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {"k", "seed", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "i|i", kwlist,
				      &self->k, &self->seed)) {
        return -1;
    }

    if (self->k < 2 || self->k > 16) {
        char * msg = "Number of registers must be in the range [2^2, 2^16]";
        PyErr_SetString(PyExc_ValueError, msg);
	return -1;
    }

    self->size = 1 << self->k;
    self->registers = (char *) calloc(self->size, sizeof(char));

    self->cache = 0;
    self->use_cache = 0;

    return 0;
}

static PyMemberDef HyperLogLog_members[] = {
    {NULL} /* Sentinel */
};

/* Adds an element to the cardinality estimator. */
static PyObject *
HyperLogLog_add(HyperLogLog *self, PyObject *args)
{
    const char *data;
    const Py_ssize_t dataLength;

    if (!PyArg_ParseTuple(args, "s#", &data, &dataLength))
        return NULL;

    uint32_t hash;
    uint32_t index;
    uint32_t rank;

    MurmurHash3_x86_32((void *) data, dataLength, self->seed, (void *) &hash);

    /* Use the first k bits as a zero based index */
    index = (hash >> (32 - self->k));

    /* Compute the rank, lzc + 1, of the remaining 32 - k bits */
    rank = leadingZeroCount((hash << self->k) >> self->k) - self->k + 1;

    if (rank > self->registers[index]) {
        self->registers[index] = rank;
        self->use_cache = 0;
        Py_RETURN_TRUE;
    }
    Py_RETURN_FALSE;
};

/* Gets a cardinality estimate. */
static PyObject *
HyperLogLog_cardinality(HyperLogLog *self)
{

    if (self->use_cache) {
        return Py_BuildValue("d", self->cache);
    }

    static const double two_32 = 4294967296.0;
    static const double neg_two_32 = -4294967296.0;
    double alpha = 0.0;

    switch (self->size) {
      case 16:
      	  alpha = 0.673;
	      break;
      case 32:
	      alpha = 0.697;
	      break;
      case 64:
	      alpha = 0.709;
	      break;
      default:
	      alpha = 0.7213/(1.0 + 1.079/(double) self->size);
          break;
    }

    uint32_t i;
    double rank;
    double sum = 0.0;

    for (i = 0; i < self->size; i++) {
        rank = (double) self->registers[i];
        sum = sum + pow(2, -1*rank);
    }

    double estimate = alpha * (1/sum) * self->size * self->size;

    if (estimate <= 2.5 * self->size) {
        uint32_t zeros = 0;
	uint32_t i;

	for (i = 0; i < self->size; i++) {
    	    if (self->registers[i] == 0) {
    	        zeros += 1;
            }
	}

        if (zeros != 0) {
            double size = (double) self->size;
            estimate = size * log(size / (double) zeros);
        }
    }

    if (estimate > (1.0/30.0) * two_32) {
        estimate = neg_two_32 * log(1.0 - estimate/two_32);
    }

    self->cache = estimate;
    self->use_cache = 1;

    return Py_BuildValue("d", estimate);
}

/* Get a Murmur3 hash of a python string, buffer or bytes (python 3.x) as an
 * unsigned integer.
 */
static PyObject *
HyperLogLog_murmur3_hash(HyperLogLog *self, PyObject *args)
{
    const char *data;
    const Py_ssize_t dataLength;

    if (!PyArg_ParseTuple(args, "s#", &data, &dataLength)) {
        return NULL;
    }

    uint32_t hash;
    MurmurHash3_x86_32((void *) data, dataLength, self->seed, (void *) &hash);
    return Py_BuildValue("i", hash);
}

/* Merges another HyperLogLog into the current HyperLogLog. The registers of
 * the other HyperLogLog are unaffected.
 */
static PyObject *
HyperLogLog_merge(HyperLogLog *self, PyObject * args)
{
    PyObject *hll;
    if (!PyArg_ParseTuple(args, "O", &hll)) {
        return NULL;
    }

    PyObject *size = PyObject_CallMethod(hll, "size", NULL);

    #if PY_MAJOR_VERSION >= 3
        long hllSize = PyLong_AsLong(size);
    #else
        long hllSize = PyInt_AS_LONG(size);
    #endif

    if (hllSize != self->size) {
        PyErr_SetString(PyExc_ValueError, "HyperLogLogs must be the same size");
        return NULL;
    }

    Py_DECREF(size);

    PyObject *hllByteArray = PyObject_CallMethod(hll, "registers", NULL);
    char *hllRegisters = PyByteArray_AsString(hllByteArray);

    self->use_cache = 0;

    uint32_t i;
    for (i = 0; i < self->size; i++) {
        if (self->registers[i] < hllRegisters[i]) {
            self->registers[i] = hllRegisters[i];
        }
    }

    Py_DECREF(hllByteArray);

    Py_INCREF(Py_None);
    return Py_None;
}

/* Support for pickling, called when HyperLogLog is serialized. */
static PyObject *
HyperLogLog_reduce(HyperLogLog *self)
{

    char *arr = (char *) malloc(self->size * sizeof(char));

    /* Pickle protocol 2, used in python 2.x, doesn't allow null bytes in
     * strings and does not support pickling bytearrays. For backwards
     * compatibility, we set all null bytes to 'z' before pickling.
     */
    int i;
    for (i = 0; i < self->size; i++) {
        if (self->registers[i] == 0) {
            arr[i] = 'z';
        }

        else {
            arr[i] = self->registers[i];
        }
    }

    PyObject *args = Py_BuildValue("(ii)", self->k, self->seed);
    PyObject *registers = Py_BuildValue("s#", arr, self->size);

    free(arr);

    return Py_BuildValue("(ONN)", Py_TYPE(self), args, registers);
}

/* Gets a copy of the registers as a bytesarray. */
static PyObject *
HyperLogLog_registers(HyperLogLog *self)
{
    PyObject *registers;
    registers = PyByteArray_FromStringAndSize(self->registers, self->size);
    return registers;
}

/* Sets register at index to rank. */
static PyObject *
HyperLogLog_set_register(HyperLogLog *self, PyObject * args)
{
    const int32_t index;
    const int32_t rank;

    if (!PyArg_ParseTuple(args, "ii", &index, &rank)) {
        return NULL;
    }

    if (index < 0) {
        char * msg = "Index is negative.";
        PyErr_SetString(PyExc_ValueError, msg);
        return NULL;
    }

    if (index > self->size - 1) {
        char * msg = "Index greater than the number of registers.";
        PyErr_SetString(PyExc_IndexError, msg);
        return NULL;
    }

    if (rank >= 32) {
        char* msg = "Value greater than than the maximum possible rank 32.";
        PyErr_SetString(PyExc_ValueError, msg);
        return NULL;
    }

    if (rank < 0) {
        char * msg = "Rank is negative.";
        PyErr_SetString(PyExc_ValueError, msg);
        return NULL;
    }

    self->use_cache = 0;
    self->registers[index] = rank;

    Py_INCREF(Py_None);
    return Py_None;

}

/* Gets the seed value used in the Murmur hash. */
static PyObject *
HyperLogLog_seed(HyperLogLog* self)
{
    return Py_BuildValue("i", self->seed);
}

/* Sets all the registers. */
static PyObject *
HyperLogLog_set_registers(HyperLogLog *self, PyObject *args)
{
    PyObject *obj;
    char* registers;
    uint32_t len;
    int i;

    if (!PyArg_ParseTuple(args, "O", &obj)) {
        return NULL;
    }

    if (PyByteArray_Check(obj)) {
        len = PyByteArray_Size(obj);
        registers = PyByteArray_AsString(obj);
    }

    else if (PyBytes_Check(obj)) {
        len = PyBytes_Size(obj);
        registers = PyBytes_AsString(obj);
    }

    else {
        char* msg = "Registers must be a bytearray or bytes type.";
        PyErr_SetString(PyExc_TypeError, msg);
        return NULL;
    }

    if (len != self->size) {
        char msg[74];
        sprintf(msg, "Invalid size. Expected %u registers received %u registers.", self->size, len);
        PyErr_SetString(PyExc_ValueError, msg);
        return NULL;
    }

    self->use_cache = 0;

    // Check for bad register values
    for (i = 0; i < self->size; i++) {
        if (registers[i] > 32) {
            char* msg = "Value greater than than the maximum possible rank (32).";
            PyErr_SetString(PyExc_ValueError, msg);
            return NULL;
        }
    }

    // Only set registers if all values are okay
    for (i = 0; i < self->size; i++) {
        self->registers[i] = registers[i];
    }

    Py_INCREF(Py_None);
    return Py_None;
}

/* Support for pickling, called when HyperLogLog is de-serialized. */
static PyObject *
HyperLogLog_set_state(HyperLogLog * self, PyObject * state)
{

    char *registers;
    if (!PyArg_ParseTuple(state, "s:setstate", &registers)) {
        return NULL;
    }

    int i;
    for (i = 0; i < self->size; i++) {
        if (registers[i] == 'z') {
            self->registers[i] = 0;
        } else {
            self->registers[i] = registers[i];
        }
    }

    Py_INCREF(Py_None);
    return Py_None;
}

/* Gets the number of registers. */
static PyObject *
HyperLogLog_size(HyperLogLog* self)
{
    return Py_BuildValue("i", self->size);
}

static PyMethodDef HyperLogLog_methods[] = {
    {"add", (PyCFunction)HyperLogLog_add, METH_VARARGS,
     "Add an element."
    },
    {"cardinality", (PyCFunction)HyperLogLog_cardinality, METH_NOARGS,
     "Get the cardinality."
    },
    {"merge", (PyCFunction)HyperLogLog_merge, METH_VARARGS,
     "Merge another HyperLogLog object with the current HyperLogLog."
    },
    {"murmur3_hash", (PyCFunction)HyperLogLog_murmur3_hash, METH_VARARGS,
     "Gets a Murmur3 hash"
    },
    {"__reduce__", (PyCFunction)HyperLogLog_reduce, METH_NOARGS,
     "Serialization function for pickling."
    },
    {"registers", (PyCFunction)HyperLogLog_registers, METH_NOARGS,
     "Get a copy of the registers as a bytearray."
    },
    {"seed", (PyCFunction)HyperLogLog_seed, METH_NOARGS,
     "Get the seed used in the Murmur3 hash."
    },
    {"set_registers", (PyCFunction)HyperLogLog_set_registers, METH_VARARGS,
     "Set the registers with a bytearray."
    },
    {"set_register", (PyCFunction)HyperLogLog_set_register, METH_VARARGS,
     "Set the register at a zero-based index to the specified rank."
    },
    {"__setstate__", (PyCFunction)HyperLogLog_set_state, METH_VARARGS,
    "De-serialization function for pickling."
    },
    {"size", (PyCFunction)HyperLogLog_size, METH_NOARGS,
     "Returns the number of registers."
    },
    {NULL}  /* Sentinel */
};

static PyTypeObject HyperLogLogType = {
    #if PY_MAJOR_VERSION >= 3
        PyVarObject_HEAD_INIT(NULL, 0)
    #else
        PyObject_HEAD_INIT(NULL)
    0,                               /* ob_size */
    #endif
    "HLL.HyperLogLog",               /* tp_name */
    sizeof(HyperLogLog),             /* tp_basicsize */
    0,                               /* tp_itemsize */
    (destructor)HyperLogLog_dealloc, /* tp_dealloc */
    0,                               /* tp_print */
    0,                               /* tp_getattr */
    0,                               /* tp_setattr */
    0,                               /* tp_compare */
    0,                               /* tp_repr */
    0,                               /* tp_as_number */
    0,                               /* tp_as_sequence */
    0,                               /* tp_as_mapping */
    0,                               /* tp_hash */
    0,                               /* tp_call */
    0,                               /* tp_str */
    0,                               /* tp_getattro */
    0,                               /* tp_setattro */
    0,                               /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT |
        Py_TPFLAGS_BASETYPE,         /* tp_flags */
    "HyperLogLog object",            /* tp_doc */
    0,		                     /* tp_traverse */
    0,		                     /* tp_clear */
    0,		                     /* tp_richcompare */
    0,		                     /* tp_weaklistoffset */
    0,		                     /* tp_iter */
    0,		                     /* tp_iternext */
    HyperLogLog_methods,             /* tp_methods */
    HyperLogLog_members,             /* tp_members */
    0,                               /* tp_getset */
    0,                               /* tp_base */
    0,                               /* tp_dict */
    0,                               /* tp_descr_get */
    0,                               /* tp_descr_set */
    0,                               /* tp_dictoffset */
    (initproc)HyperLogLog_init,      /* tp_init */
    0,                               /* tp_alloc */
    HyperLogLog_new,                 /* tp_new */
};

#if PY_MAJOR_VERSION >= 3
    static PyModuleDef HyperLogLogmodule = {
        PyModuleDef_HEAD_INIT,
        "HyperLogLog",
        "A space efficient cardinality estimator (v1.2).",
        -1,
        NULL, NULL, NULL, NULL, NULL
    };
#else
    static PyMethodDef module_methods[] = {
        {NULL}  /* Sentinel */
    };
#endif

#if PY_MAJOR_VERSION >=3
    PyMODINIT_FUNC
    PyInit_HLL(void)
#else
    /* declarations for DLL import/export */
    #ifndef PyMODINIT_FUNC
        #define PyMODINIT_FUNC void
    #endif
    PyMODINIT_FUNC initHLL(void)
#endif

{
    PyObject* m;
    #if PY_MAJOR_VERSION >= 3
        if (PyType_Ready(&HyperLogLogType) < 0) {
            return NULL;
        }

        m = PyModule_Create(&HyperLogLogmodule);

        if (m == NULL) {
            return NULL;
        }
    #else
        if (PyType_Ready(&HyperLogLogType) < 0) {
            return;
        }

        char *description = "HyperLogLog cardinality estimator.";
        m = Py_InitModule3("HLL", module_methods, description);

        if (m == NULL) {
            return;
        }
    #endif

    Py_INCREF(&HyperLogLogType);
    PyModule_AddObject(m, "HyperLogLog", (PyObject *)&HyperLogLogType);

    #if PY_MAJOR_VERSION >= 3
        return m;
    #endif
}

/* Get the number of leading zeros. */
uint32_t leadingZeroCount(uint32_t x) {
    x |= (x >> 1);
    x |= (x >> 2);
    x |= (x >> 4);
    x |= (x >> 8);
    x |= (x >> 16);
    return (32 - ones(x));
}

/* Get the number of bits set to 1. */
uint32_t ones(uint32_t x) {
    x -= (x >> 1) & 0x55555555;
    x = ((x >> 2) & 0x33333333) + (x & 0x33333333);
    x = ((x >> 4) + x) & 0x0F0F0F0F;
    x += (x >> 8);
    x += (x >> 16);
    return(x & 0x0000003F);
}
