
from .util import *
from .parse import Parser

from importlib import import_module
from warnings import warn
from os import getcwd
import os.path as op
import json
import nxp
import sys

# ------------------------------------------------------------------------

from nxp.error import ScopeError, TagError, LengthError

class Compiler:
    __slots__ = ('_pre','_doc','_var','_fmt','_path','_indoc')
    def __init__( self ):
        self._pre = dict()
        self._doc = dict()
        self._var = PrefixTree('warn')
        self._fmt = None
        self._path = [ getcwd() ]
        self._indoc = False

        sys.path.insert( 0, getcwd() )
        self.load('melan.builtin',dom='')

    def __str__(self):
        pre = ', '.join([ self._pre.keys() ])
        doc = ', '.join([ self._doc.keys() ])
        var = ', '.join([ self._var.keys() ])

        return '\n'.join([
            'MeLan compiler', 
            '+ Path:\n\t' + ' ; '.join(self._path),
            f'+ Variables ({len(self._var)}):\n\t{var}',
            f'+ Preamble ({len(self._pre)}):\n\t{pre}',
            f'+ Document ({len(self._doc)}):\n\t{doc}'
        ])

    def _chkdir(self,p):
        assert op.isdir(p), FileNotFoundError(f'Not a folder: {p}')

    def _chkcmd(self,cmd):
        assert isinstance(cmd,dict), \
            TypeError(f'Expected dict, but got "{type(cmd)}" instead.')
        assert all([ callable(f) for f in cmd.values() ]), \
            TypeError('Command values should be callable.')
        
    def _chktags(self,first,last):
        assert first.tag == last.tag[1:], TagError( f'{first.tag} vs. {last.tag}', 'Tag mismatch between first and last elements.' )

    # ----------  =====  ----------
    # main functions

    def process(self,buffer,first=(0,0),last=None):
        return nxp.process( Parser, self._callback, buffer, first, last )

    def procfile(self,infile,r2l=False):
        infile = self.pathFind(infile)
        return nxp.procfile( Parser, self._callback, infile, r2l )

    def proctxt(self,text,r2l=False):
        return nxp.proctxt( Parser, self._callback, text, r2l )

    def format(self,text):
        return text if self._fmt is None else self._fmt(self,text)

    # ----------  =====  ----------
    # variables

    def varAdd(self,var,prefix=''): 
        # convert to dict
        if isinstance(var,str):
            assert op.isfile(var), FileNotFoundError(var)
            assert var.endswith('.json'), ValueError('Not a JSON file.')
            with open(var) as fh:
                return json.load(fh)
        
        assert isinstance(var,dict), TypeError(f'Bad var type: {type(var)}')

        # insert each item
        for k,v in var.items():
            self._var.insert( prefix+k, v )

        return self
    def varFilt(self,prefix):
        return { k.lstrip(prefix): v for k,v in self._var.filter(prefix) }

    def lst(self,key): return self._var.setdefault(key,[])
    def arg(self,key): return self._var.setdefault(key,{})
    def num(self,key): return self._var.setdefault(key,0)
    def get(self,key,default=None): return self._var.setdefault(key,default)

    def __getitem__(self,key): 
        return self._var[key]
    def __setitem__(self,key,val): 
        self._var[key] = val
    def __contains__(self,key):
        return key in self._var

    # ----------  =====  ----------
    # path, files, and extensions

    def pathAppend(self,p):
        self._chkdir(p)
        self._path.append(p)
        return self
    def pathPrepend(self,p):
        self._chkdir(p)
        self._path.insert(0,p)
        return self
    def pathFind(self,f):
        for p in self._path:
            q = op.join(p,f)
            if op.exists(q):
                return q
        raise FileNotFoundError(f)

    def readfile(self,f):
        with open(self.pathFind(f)) as fh:
            return fh.read()

    def load(self,pkg,prefix='',package=None,dom='melan_'):

        # remove .py extension
        if pkg.endswith('.py') and op.isfile(pkg):
            pkg = pkg.rstrip('.py')

        # import module and look for "export"
        x = import_module( dom+pkg, package )
        try:
            x = x.export 
        except:
            raise RuntimeError('Module should define variable "export".')

        # add commands and variables
        if 'pre' in x: self.preAdd(x['pre'],prefix)
        if 'doc' in x: self.docAdd(x['doc'],prefix)
        if 'var' in x: self.varAdd(x['var'])
        if 'fmt' in x: 
            if self._fmt is not None:
                 warn( 'Format override', Warning )
            self._fmt = x['fmt']

        return x

    # ----------  =====  ----------
    # commands

    def docAdd(self,cmd,prefix=''):
        self._chkcmd(cmd)
        for name,fun in cmd.items():
            name = prefix+name
            if name in self._doc:
                warn( f'Command override (doc): {name}', Warning )
            self._doc[name] = fun
        return self

    def preAdd(self,cmd,prefix=''):
        self._chkcmd(cmd)
        for name,fun in cmd.items():
            name = prefix+name
            if name in self._pre:
                warn( f'Command override (pre): {name}', Warning )
            self._pre[name] = fun
        return self

    # ----------  =====  ----------
    # processing callback

    def _callback(self,tsf,elm):
        if isinstance(elm,nxp.RMatch):
            beg,end = elm.beg, elm.end
            tag = elm.tag 

            if tag == 'rep':
                tsf.sub( beg, end, elm.text )
            elif tag == 'var':
                tsf.sub( beg, end, self[elm.data[1]] )
            else:
                raise TagError(tag,'Unknown tag')
        elif elm.name == 'command':
            self._cb_cmd(tsf,elm)
        elif elm.name == 'document':
            self._cb_doc(tsf,elm)
        else:
            raise ScopeError(elm.name,'Unexpected scope')

    def _cb_doc(self,tsf,elm):
        assert not self._indoc, RuntimeError('[bug] Nested document?')
        assert len(elm) >= 2, LengthError(elm)

        # bounds
        self._chktags( elm[0], elm[-1] )
        tsf.restrict( elm[0].end, elm[-1].beg )
        
        # process
        self._indoc = True
        for sub in elm[1:-1]: self._callback(tsf,sub)
        self._indoc = False
        
    def _cb_cmd(self,tsf,elm):
        assert len(elm) <= 3, LengthError(elm)

        # command name
        match = elm[0]
        assert match.tag == 'cmd', TagError(match.tag)

        name = match.data[1]
        beg,end = match.beg, match.end

        # body and options
        body = ''
        opt = dict()
        buf = tsf.buffer

        for sub in elm[1:]:
            assert isinstance(sub,nxp.RNode), TypeError(sub)
            if sub.name == 'command.option':
                _,e,opt = self._cb_opt(buf,sub)
            else:
                _,e,body = self._cb_body(buf,sub)
            
            if e > end: end = e

        # call command
        if self._indoc:
            tsf.sub( beg, end, self._doc[name](body,**opt) )
        else:
            self._pre[name](self,body,**opt)

    def _cb_opt(self,buf,elm):
        assert len(elm) >= 2, LengthError(elm,'Insufficient length')

        # bounds
        self._chktags( elm[0], elm[-1] )
        beg, end = elm[0].beg, elm[-1].end

        # options
        out = dict()
        for sub in elm[1:-1]:
            assert sub.name == 'command.option.name', ScopeError(sub.name)
            assert 1 <= len(sub) <= 2, LengthError(sub)
            assert sub[0].tag == 'opt', TagError(sub[0].tag)

            name = sub[0].text
            if len(sub) > 1:
                out[name] = self._cb_val(buf,sub[1])
            else:
                out[name] = True 

        return beg,end,out

    def _cb_val(self,buf,elm):
        assert elm.name.startswith('command.option.'), ScopeError(elm.name)
        tag = elm[0].tag 
        if tag == 'num':
            return float(elm[0].text)
        elif tag == 'bool':
            txt = elm[0].text.lower()
            return { 'true': True, 'false': False }[txt]
        else:
            return self._cb_str(buf,elm)

    def _cb_str(self,buf,elm):
        assert len(elm) >= 2, LengthError(elm,'Insufficient length')

        # process matches within quotes
        tsf = nxp.Transform( buf, elm[0].end, elm[-1].beg )
        for sub in elm[1:-1]: self._callback(tsf,sub)
        return str(tsf)

    def _cb_body(self,buf,elm):
        assert len(elm) >= 2, LengthError(elm,'Insufficient length')

        # beginning/end of body delimiters
        self._chktags( elm[0], elm[-1] )
        beg = elm[0].beg 
        end = elm[-1].end
        
        # process matches within delimiters
        tsf = nxp.Transform( buf, elm[0].end, elm[-1].beg )
        if elm.name in {'command.body_curly','command.body_square'}:
            for sub in elm[1:-1]: self._callback(tsf,sub)

        # remove common indent for multiline bodies
        return beg,end,dedent(str(tsf))

# ------------------------------------------------------------------------

def compile( infile, r2l=False, output=None, show=False ):
    
    # compile document
    cpl = Compiler()
    out = cpl.procfile(infile,r2l)
    txt = cpl.format(str(out))

    # print to console
    if show: print(txt)

    # write to file
    if output:
        with open(output,'w') as fh:
            fh.write(txt)

    return txt
    