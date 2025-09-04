#include <Python.h>

PyMODINIT_FUNC
PyInit_crypto(void)
{
    PyObject *tmp;
    if (!(tmp = PyImport_ImportModule("a12de8d4beb198db8e1f__mypyc"))) return NULL;
    PyObject *capsule = PyObject_GetAttrString(tmp, "init_faster_eth_utils___crypto");
    Py_DECREF(tmp);
    if (capsule == NULL) return NULL;
    void *init_func = PyCapsule_GetPointer(capsule, "a12de8d4beb198db8e1f__mypyc.init_faster_eth_utils___crypto");
    Py_DECREF(capsule);
    if (!init_func) {
        return NULL;
    }
    return ((PyObject *(*)(void))init_func)();
}

// distutils sometimes spuriously tells cl to export CPyInit___init__,
// so provide that so it chills out
PyMODINIT_FUNC PyInit___init__(void) { return PyInit_crypto(); }
