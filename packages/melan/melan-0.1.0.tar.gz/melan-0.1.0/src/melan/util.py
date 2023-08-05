
import re
import math
from warnings import warn

# ------------------------------------------------------------------------

def _indent_length(line,pat):
    L = len(pat.match(line)[0])
    return L if L < len(line) else math.inf

def splitlines(text):
    return re.split( r'\r?\n', text )

def dedent(body):

    # split into lines
    lines = splitlines(body)
    if len(lines)==1: return lines[0]

    # remove last white line
    if len(lines[-1].strip()) == 0:
        lines.pop()

    # find common white prefix
    white = re.compile(r'^\s*')
    indent = min([ _indent_length(line,white) for line in lines[1:] ])
    if indent == math.inf: indent = 0 # all blank lines

    # return transformed output
    for k,line in enumerate(lines):
        if k==0: continue 
        lines[k] = line[indent:]

    return '\n'.join(lines)

# ------------------------------------------------------------------------

class PrefixNode:
    __slots__ = ('data','child','terminal')
    def __init__(self,data=None):
        self.data = None
        self.child = dict()
        self.terminal = False

    def get(self,key):
        return self.child[key]

    def set(self,key,data=None):
        node = PrefixNode(data)
        self.child[key] = node
        return node

    def items(self,pfx=''):
        if self.terminal:
            yield pfx, self.data 
        for k,c in self.child.items():
            p = pfx+k
            if c.terminal: 
                yield p, c.data
            yield from c.items(p)

    def keys(self,pfx=''):
        if self.terminal:
            yield pfx
        for k,c in self.child.items():
            p = pfx+k
            if c.terminal: 
                yield p
            yield from c.keys(p)

    def values(self):
        if self.terminal:
            yield self.data
        for c in self.child.values():
            if c.terminal: 
                yield c.data
            yield from c.values()

# ------------------------------------------------------------------------

class PrefixTree:
    __slots__ = ('root','len','dup')
    def __init__(self,dup='ok'):
        self.root = PrefixNode(None)
        self.len = 0
        self.dup = dup

    def __len__(self):
        return self.len
    def __getitem__(self,name):
        return self.find(name).data 
    def __setitem__(self,name,value):
        self.insert(name,value)
    def __contains__(self,name):
        return self.has(name)

    def _duplicate(self,name):
        if self.dup.startswith('warn'):
            warn( f'Key will be overwritten: {name}', RuntimeWarning )
        elif self.dup.startswith('err'):
            raise KeyError( f'Key cannot be overwritten: {name}' )

    def items(self):
        yield from self.root.items()
    def keys(self):
        yield from self.root.keys()
    def values(self):
        yield from self.root.values()
    def filter(self,prefix):
        try:
            yield from self.find(prefix).items()
        except:
            raise StopIteration()

    def __str__(self):
        return str({ k:v for k,v in self.items() })

    def find(self,name):
        cur = self.root
        for c in name:
            try:
                cur = cur.get(c)
            except:
                raise KeyError(f'Not found: {name}')
        return cur

    def has(self,name):
        try:
            return self.find(name).terminal 
        except:
            return False

    def insert(self,name,data):
        cur = self.root
        for c in name:
            try:
                cur = cur.get(c)
            except:
                cur = cur.set(c,None)

        cur.data = data
        if cur.terminal:
            self._duplicate(name)
        else:
            cur.terminal = True
            self.len += 1
            
    def setdefault(self,name,data):
        cur = self.root
        for c in name:
            try:
                cur = cur.get(c)
            except:
                cur = cur.set(c,None)

        if not cur.terminal:
            cur.terminal = True
            cur.data = data 
            self.len += 1

        return cur.data
