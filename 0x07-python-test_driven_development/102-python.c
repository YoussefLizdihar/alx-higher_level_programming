#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    printf("[.] string object info\n");

    // Check if the object is a valid string
    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Get the type of the Unicode object
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    const char *type = "compact unicode object";

    // Check if the string is compact ASCII
    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        type = "compact ascii";
    }

    // Get the string value
    PyObject *ascii_value = PyUnicode_AsASCIIString(p);
    const char *value = PyBytes_AsString(ascii_value);

    // Print the information
    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %s\n", value);

    // Decrement the reference count of the temporary PyObject
    Py_XDECREF(ascii_value);
}

