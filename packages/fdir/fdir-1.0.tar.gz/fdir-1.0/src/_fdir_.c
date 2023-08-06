#include "_fdir_.h"
#include "_error_types_.h"

char * to_string(int n)
{
	char *c = PyBytes_AS_STRING(PyBytes_FromFormat("%d",n));

	return c;
}
char *_dot(int n)
{
	char *c = PyBytes_AS_STRING(PyBytes_FromFormat("%.*s", n, "."));

	return c;
}
int is_file(char *path) // This function wasn't used
{
    struct stat st_path;
    stat(path, &st_path);
    return S_ISREG(st_path.st_mode);
}
int file_extention(char *file_name,char *key)
{
	int size = strlen(file_name);
	int step = strlen(key);
	int ind = 0;
	for(int i= size - step;i<size;i++)
	{
		if(key[ind]!=file_name[i])
			return 0;
		ind++;
	}
	return 1;
}
int is_dir(char *path)
{
	int size = strlen(path);

	for(int i=size - 1;i>=0;i--)
	{
		if(path[i]=='.')
			return 0;
		else if(path[i]=='/')
			break;
	}

	return 1;
}
int is_mode(char *file_name , char *mode)
{
    if(!strcmp(mode,"//"))
        return 1;

	else if(!strcmp(mode,"."))
        if(!is_dir(file_name))		
            return 1;
        else
            return 0;

	else if(!strcmp(mode,"./"))
        if(is_dir(file_name))
		    return 1;
        else
            return 0;

	else if(mode[0] == '.')
        if(!is_dir(file_name) && file_extention(file_name, mode))
		    return 1;
        else
            return 0;
    else
        return 0;
}           
size_t list_size(PyObject *lst)
{

	if(PyList_Check(lst))
		return (size_t)PyList_GET_SIZE(lst);
	else
		return 0;
}
void py_err_msg(PyObject *type,const char *c)
{   
    PyErr_SetString(type,c);
}

PyObject *_walk_(char *current_dir , char *mode,PyObject *list)
{
	if(!is_dir(current_dir))
    {
        Py_INCREF(list);
        return list;
    }

    DIR *dir;
    struct dirent *curr_dir;

    dir = opendir(current_dir);
    while ((curr_dir=readdir(dir)) != NULL) {
        if (!strcmp(curr_dir->d_name, ".") || !strcmp(curr_dir->d_name, "..") || curr_dir->d_type == DT_UNKNOWN)
        {
        	continue;
        }
        else
        { 
            if(curr_dir->d_type == DT_DIR)
            {
                char *tmp = PyBytes_AS_STRING(PyBytes_FromFormat("%s/%s",current_dir,curr_dir->d_name));
               _walk_(tmp,mode,list);
            }
            if(is_mode(curr_dir->d_name,mode))
            {
        	    int added =  PyList_Append(list,PyUnicode_FromString(PyBytes_AS_STRING(PyBytes_FromFormat("%s/%s",current_dir,curr_dir->d_name))));

        	    if(added == -1)
                    py_err_msg(MODULE_ERROR,"Unhandled Exception : PyList_Append(...)");
            }
        }
    }
    closedir(dir);

    Py_INCREF(list);

    return list;
}

PyObject *_listdir_(char *current_dir , char *mode)
{
	if(!is_dir(current_dir))
    {
        py_err_msg(VALUE,"Path Not File");
        return NULL;
    }
	PyObject *list = PyList_New(0);

    DIR *dir;
    struct dirent *curr_dir;
    char * fileInfo;

    dir = opendir(current_dir);
    while ((curr_dir=readdir(dir)) != NULL) {
        if (!strcmp(curr_dir->d_name, ".") || !strcmp(curr_dir->d_name, "..") || curr_dir->d_type == DT_UNKNOWN)
        {
        	continue;
        }
        else if(is_mode(curr_dir->d_name,mode))
        {
        	fileInfo = curr_dir->d_name;
        	int added =  PyList_Append(list,PyUnicode_FromString(PyBytes_AS_STRING(PyBytes_FromFormat("%s/%s",current_dir,fileInfo))));

        	if(added == -1)
                py_err_msg(MODULE_ERROR,"Unhandled Exception : PyList_Append(...)");

        }
    }
    closedir(dir);

    Py_INCREF(list);

    return list;
}
PyObject *_itrAll_(PyObject *current_list,char *mode)
{

	PyObject *map = PyDict_New();
	size_t size = list_size(current_list);
	for(size_t i=0;i<size;i++)
	{
		char *c = PyUnicode_AsUTF8 ( PyList_GET_ITEM(current_list , i) ) ;
        char *cnum = to_string(i);
        PyObject *tmp_lst  =_listdir_(c,mode);
        
        if(list_size(tmp_lst) == 0)
        {
            Py_DecRef(tmp_lst);
            continue;
        }

		PyDict_SetItemString(map,cnum,tmp_lst);
    	Py_DecRef(tmp_lst);
	}
	Py_DecRef(current_list);

	Py_INCREF(map);

	return map;
}

static PyObject *fdir_listdir(PyObject *self , PyObject *args )
{
	char *current_dir;
	char *mode;

	if(!PyArg_ParseTuple(args , "ss" ,&current_dir,&mode))
		return NULL;


	PyObject *list =  Py_BuildValue("O",_listdir_(current_dir,mode));


	return list;
}
static PyObject *fdir_itrAll(PyObject *self , PyObject *args)
{
	char *mode;
	PyObject *current_list;

	if(!PyArg_ParseTuple(args , "Os" , &current_list,&mode))
		return NULL;
	if(!PyList_Check(current_list))
		return NULL;

    PyObject *dict = Py_BuildValue("O",_itrAll_(current_list,mode)); 

	return dict;
}

static PyObject *fdir_itrDict(PyObject *self , PyObject *args)
{
	char *mode;
	PyObject *current_dict;
	if(!PyArg_ParseTuple(args , "Os" , &current_dict,&mode))
		return NULL;
	if(!PyDict_Check(current_dict))
		return NULL;

	PyObject *map = PyDict_New();
	PyObject *keys = PyDict_Keys(current_dict);
	size_t size = list_size(keys);

	for(size_t i=0;i<size;i++)
	{
		char *k = PyUnicode_AsUTF8 ( PyList_GET_ITEM(keys , i) ) ;
		PyObject *lst  = PyDict_GetItemString(current_dict, k);
		PyObject *sub_dict = _itrAll_(lst,mode);

		PyDict_SetItemString(map,k,sub_dict);

		Py_DecRef(lst);
		Py_DecRef(sub_dict);
	}

	Py_DecRef(current_dict);
    
    PyObject *newDict = Py_BuildValue("O",map);

    return newDict;
}

static PyObject *fdir_walk(PyObject *self,PyObject *args)
{
	char *current_dir;
	char *mode;

	if(!PyArg_ParseTuple(args , "ss" ,&current_dir,&mode))
		return NULL;

	PyObject *empty_list = PyList_New(0);

	PyObject *list =  Py_BuildValue("O",_walk_(current_dir,mode,empty_list));

	Py_DecRef(empty_list);

	return list;
}
