#include <stdio.h>
#include "Python.h"
#include <float.h>

/**
 * print_python_bytes - prints info about a python bytes object
 * @p: a bytes object
 */
void print_python_bytes(PyObject *p)
{
	int i;
	PyBytesObject *obj = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", obj->ob_base.ob_size);
	printf("  trying string: %s\n", obj->ob_sval);
	if (obj->ob_base.ob_size > 10)
		printf("  first 10 bytes: ");
	else
		printf("  first %ld bytes: ", obj->ob_base.ob_size + 1);
	for (i = 0; i < 10; i++)
	{
		if (i == obj->ob_base.ob_size || i == 9)
		{
			printf("%.2x", obj->ob_sval[i] & 0xff);
			break;
		}
		printf("%.2x ", obj->ob_sval[i] & 0xff);
	}
	printf("\n");
}

/**
 * print_python_float - prints info about a python float object
 * @p: pointer to pyobject
 */
void print_python_float(PyObject *p)
{
	int ipart;
	PyFloatObject *obj = (PyFloatObject *)p;
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(obj))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	value = obj->ob_fval;
	ipart = (int)value;
	value = value - ipart;
	printf("%d.", ipart);
	while (value > 0.0)
	{
		value = value * 10;
		ipart = (int)ipart;
		value = value - ipart;
		printf("%d", ipart);
	}
	printf("\n");
}

/**
 * print_python_list - prints info about a python bytes object
 * @p: a bytes object
 */
void print_python_list(PyObject *p)
{
	int i;
	PyListObject *ll = (PyListObject *)p;
	PyVarObject ob_base = ll->ob_base;
	PyObject *member;
	const char *tp_name;

	printf("[*] Python list info\n");
	if (!PyList_CheckExact(ll))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", ob_base.ob_size);
	printf("[*] Allocated = %ld\n", ll->allocated);
	for (i = 0; i < ob_base.ob_size; i++)
	{
		member = ll->ob_item[i];
		tp_name = member->ob_type->tp_name;
		printf("Element %d: %s\n", i, tp_name);
		if (strcmp(tp_name, "bytes") == 0)
			print_python_bytes(member);
		else if (strcmp(tp_name, "float") == 0)
			print_python_float(member);
	}
}
