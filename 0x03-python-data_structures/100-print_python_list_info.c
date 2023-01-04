#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints information about a python list
 * @p: pointer to the python list
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *ll = (PyListObject *)p;
	PyVarObject ob_base = ll->ob_base;
	PyObject *member;

	printf("[*] Size of the Python List = %ld\n", ob_base.ob_size);
	printf("[*] Allocated = %ld\n", ll->allocated);
	for (i = 0; i < ob_base.ob_size; i++)
	{
		member = ll->ob_item[i];
		printf("Element %d: %s\n", i, member->ob_type->tp_name);
	}
}
