
import os.path as op
import json
import sys 

# ------------------------------------------------------------------------

def addpath(cpl,path,before=False):
    assert op.isdir(path), NotADirectoryError(f'Not a folder: {path}')
    if before:
        cpl.pathPrepend(path)
    else:
        cpl.pathAppend(path)

def pypath(cpl,path,before=False):
    assert op.isdir(path), NotADirectoryError(f'Not a folder: {path}')
    if before:
        sys.path.insert(0,path)
    else:
        sys.path.append(path)

def usepkg(cpl,path,prefix='',package=None):
    cpl.load(path,prefix=prefix,package=package)

def define(cpl,body=None,file=None):
    if body:
        cpl.varAdd(json.loads(body))
    if file:
        cpl.varAdd(file)

def insert(cpl,body):
    return cpl.readfile(body)

def include(cpl,body,r2l=False):
    return cpl.procfile(body,r2l)

def inject(body):
    return body

# ------------------------------------------------------------------------

export = {
    'pre': {
        'addpath': addpath,
        'pypath': pypath,
        'usepkg': usepkg,
        'define': define,
        'insert': insert,
        'include': include
    },
    'doc': { 'insert': inject }
}
