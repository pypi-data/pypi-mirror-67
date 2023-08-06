/*
 * fdir.h
 *
 *  Created on: Feb 13, 2020
 *      Author: Mohamed Zayan
 */

#ifndef FDIR__H_
#define FDIR__H_

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

#define PY_SSIZE_T_CLEAN
#include<python3.6m/Python.h>

typedef enum {true, false} bool;

static char module_docstring[] =
    "Files and Directories Handler C Optimized Module "
    "Functions For Iterating OS Files and Directories Faster"
    "Than Python Modules (eg : os.listdir)";

static char listdir_docstring[]=
    "Iterating OS Files and Directories For Given Path"
    "Return List of Paths From Starting Directory";

static char itrAll_docstring[]=
    "Input List of Paths Iterating OS Files and Directories "
    "For Given Path, Return dictionary";

static char itrDict_docstring[]=
	"Input dictionary of Paths Iterating OS Files and Directories "
	"For Given Path, Return dictionary";

static char walk_docstring[]=
		"Iterating through OS Files and Directories For Given Path "
		" Recursively Searching For Files of Specific Extension ( Mode )";

static PyObject* fdir_listdir(PyObject *self , PyObject *args);
static PyObject* fdir_itrAll(PyObject *self , PyObject *args);
static PyObject* fdir_itrDict(PyObject *self , PyObject *args);
static PyObject* fdir_walk(PyObject *self , PyObject *args);


static PyMethodDef module_methods[]= {
		{"listdir",fdir_listdir,METH_VARARGS,listdir_docstring},
		{"itrAll",fdir_itrAll,METH_VARARGS,itrAll_docstring},
		{"itrDict",fdir_itrDict,METH_VARARGS,itrDict_docstring},
		{"walk",fdir_walk,METH_VARARGS,walk_docstring},
		{NULL,NULL,0,NULL}
};

static struct PyModuleDef fdir =
{
		PyModuleDef_HEAD_INIT,
		"fdir",
		module_docstring,
		-1,
		module_methods

};
PyMODINIT_FUNC PyInit_fdir(void)
{
    return PyModule_Create(&fdir);
}

#endif /* FDIR__H_ */
