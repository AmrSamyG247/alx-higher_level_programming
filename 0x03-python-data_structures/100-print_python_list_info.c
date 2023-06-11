#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * includes listobject.h
 * includes object.h
 * print_python_list_info C function that-
 * prints some basic info about Python lists.
 * @p: is paython list object
**/


void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of Python List = %li\n", size);
	printf("[*] Allocated = %li\n", object->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(object->ob_item[i])->tp_name);
}

