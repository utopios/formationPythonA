#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject * my_c_module_fib(PyObject *self, PyObject *args)
{
    unsigned n;
    if (!PyArg_ParseTuple(args, "I", &n))
        return NULL;

    PyObject* fib_lst = PyList_New(0);

    if (n >= 1)
        PyList_Append(fib_lst, PyLong_FromUnsignedLong(0));
    if (n >= 2)
        PyList_Append(fib_lst, PyLong_FromUnsignedLong(1));

    for (unsigned i = 2; i < n; ++i)
    {
        unsigned long a = PyLong_AsUnsignedLong(PyList_GetItem(fib_lst, i-2));
        unsigned long b = PyLong_AsUnsignedLong(PyList_GetItem(fib_lst, i-1));

        PyList_Append(fib_lst, PyLong_FromUnsignedLong(a+b));
    }


    return fib_lst;
}

static PyMethodDef my_c_module_methods[] = {
        {"fib",  my_c_module_fib, METH_VARARGS, "Returns a list with the first n Fibonacci numbers."},
        {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef my_c_module = {
        PyModuleDef_HEAD_INIT,
        "my_c_module",   /* name of module */
        "My first Python module in C", /* module documentation, may be NULL */
        -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
        my_c_module_methods
};

PyMODINIT_FUNC PyInit_my_c_module(void)
{
    return PyModule_Create(&my_c_module);
}