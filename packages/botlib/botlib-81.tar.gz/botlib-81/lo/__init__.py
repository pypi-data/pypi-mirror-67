# LIBOBJ - library to manipulate objects.
#
#

"""object."""

__version__ = 9

import collections
import datetime
import json
import lo
import lo.typ
import logging
import os
import random
import sys
import time
import types
import _thread

from json import JSONEncoder, JSONDecoder

def __dir__():
    return ("Cfg", "Command", "Db", "Default", "Object", "cdir", "hook", "locked", "stamp", "strip", "workdir")

cache = {}
lock = _thread.allocate_lock()
hooklock = _thread.allocate_lock()
starttime = time.time()
typecheck = False
workdir = ""

timestrings = [
    "%a, %d %b %Y %H:%M:%S %z",
    "%d %b %Y %H:%M:%S %z",
    "%d %b %Y %H:%M:%S",
    "%a, %d %b %Y %H:%M:%S",
    "%d %b %a %H:%M:%S %Y %Z",
    "%d %b %a %H:%M:%S %Y %z",
    "%a %d %b %H:%M:%S %Y %z",
    "%a %b %d %H:%M:%S %Y",
    "%d %b %Y %H:%M:%S",
    "%a %b %d %H:%M:%S %Y",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%dt%H:%M:%S+00:00",
    "%a, %d %b %Y %H:%M:%S +0000",
    "%d %b %Y %H:%M:%S +0000",
    "%d, %b %Y %H:%M:%S +0000"
]

def hooked(d):
    """convert dict with stamp to it's object."""
    if "stamp" in d:
        t = d["stamp"].split(os.sep)[0]
        o = lo.typ.get_cls(t)()
    else:
        o = Object()
    o.update(d)
    return o

def locked(lock):
    """lock function on provided lock."""
    def lockeddec(func, *args, **kwargs):
        def lockedfunc(*args, **kwargs):
            lock.acquire()
            res = None
            try:
                res = func(*args, **kwargs)
            finally:
                lock.release()
            return res
        return lockedfunc
    return lockeddec

class EJSON(Exception):
    """wrong json."""
    pass

class ENOCLASS(Exception):
    """no such class."""
    pass

class ENOFILE(Exception):
    """no such file."""
    pass
    
class EOVERLOAD(Exception):
    """overloading is not permitted."""
    pass
    
class ETYPE(Exception):
    """wrong type."""
    pass

class ObjectEncoder(JSONEncoder):

    """ encode an object to string."""

    def default(self, o):
        if isinstance(o, Object):
            return vars(o)
        if isinstance(o, dict):
            return o.items()
        if isinstance(o, list):
            return iter(o)
        if type(o) in [str, True, False, int, float]:
            return o
        return repr(o)

class ObjectDecoder(JSONDecoder):

    """decode a string to an object."""

    def decode(self, s):
        if s == "":
            return Object()
        return json.loads(s, object_hook=hooked)

class O:

    """basic object."""

    __slots__ = ("__dict__", "_path")

    def __init__(self, *args, **kwargs):
        super().__init__()
        stime = str(datetime.datetime.now()).replace(" ", os.sep)
        self._path = os.path.join(lo.typ.get_type(self), stime)
        return self

    def __delitem__(self, k):
        del self.__dict__[k]
        return self.__dict__[k]
        
    def __getitem__(self, k):
        return self.__dict__[k]

    def __iter__(self):
        return iter(self.keys())

    def __len__(self):
        return len(self.__dict__)

    def __lt__(self, o):
        return len(self) < len(o)

    def __setitem__(self, k, v):
        self.__dict__[k] = v
        return self.__dict__[k]

    def get(self, k, d={}):
        return self.__dict__.get(k, d)

    def keys(self):
        return self.__dict__.keys()

    def merge(self, o, vals={}):
        return self.update(strip(self, vals))

    def update(self, d):
        return self.__dict__.update(d)
        
    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def json(self):
        return json.dumps(self, cls=ObjectEncoder, indent=4, sort_keys=True)

    def set(self, k, v):
        self.__dict__[k] = v

class Object(O):

    """big O object."""

    def __init__(self, *args, **kwargs):
        super().__init__()
        if args:
            try:
                self.update(args[0])
            except TypeError:
                self.update(vars(args[0]))
        if kwargs:
            self.update(kwargs)

    def __str__(self):
        return self.json()

    def edit(self, setter, skip=False):
        """edit with setter dict."""
        try:
            setter = vars(setter)
        except:
            pass
        if not setter:
            setter = {}
        count = 0
        for key, value in setter.items():
            if skip and value == "":
                continue
            count += 1
            if value in ["True", "true"]:
                self[key] = True
            elif value in ["False", "false"]:
                self[key] = False
            else:
                self[key] = value
        return count

    def find(self, val):
        """see if val is in one of the object's items."""
        for item in self.values():
            if val in item:
                return True
        return False

    def format(self, keys=None):
        """format tis object into a displayable string."""
        if keys is None:
            keys = vars(self).keys()
        res = []
        txt = ""
        for key in keys:
            if key == "stamp":
                continue
            val = self.get(key, None)
            if not val:
                continue
            val = str(val)
            if key == "text":
                val = val.replace("\\n", "\n")
            res.append(val)
        for val in res:
            txt += "%s%s" % (val.strip(), " ")
        return txt.strip()

    def last(self, strip=False):
        """update this object to the lastest of it's types on disk."""
        db = lo.Db()
        path, l = db.last_fn(str(lo.typ.get_type(self)))
        if l:
            if strip:
                self.update(strip(l))
            else:
                self.update(l)
            self._path = path

    @locked(lock)
    def load(self, path, force=False):
        """load from file."""
        assert path
        assert workdir
        lpath = os.path.join(workdir, "store", path)
        if not os.path.exists(lpath):
            cdir(lpath)
        #if not force and path in cache:
        #    logging.debug("cache %s" % path)
        #    return cache[path]
        logging.debug("load %s" % path)
        self._path = path
        with open(lpath, "r") as ofile:
            try:
                val = json.load(ofile, cls=ObjectDecoder)
            except json.decoder.JSONDecodeError as ex:
                raise EJSON(str(ex) + " " + lpath)
            if typecheck:
                ot = val.__dict__["stamp"].split(os.sep)[0]
                t = lo.typ.get_cls(ot)
                if type(self) != t:
                    raise ETYPE(type(self), t)
            try:
                del val.__dict__["stamp"]
            except KeyError:
                pass
            self.update(val.__dict__)
        #cache[self._path] = self
        #return cache[self._path]
        return self


    @locked(lock)
    def save(self, stime=None):
        """save to file."""
        assert workdir
        if stime:
            self._path = os.path.join(lo.typ.get_type(self), stime) + "." + str(random.randint(1, 100000))
        opath = os.path.join(workdir, "store", self._path)
        lo.cdir(opath)
        logging.debug("save %s" % self._path)
        #if self._path in cache:
        #    o = cache[self._path]
        #else:
        #    o = self
        with open(opath, "w") as ofile:
            json.dump(stamp(self), ofile, cls=ObjectEncoder, indent=4, sort_keys=True)
        return self._path

    def search(self, match=None):
        """search stringified values for a match."""
        res = False
        if match == None:
            return res
        for key, value in match.items():
            val = self.get(key, None)
            if val:
                if not value:
                    res = True
                    continue
                if value in str(val):
                    res = True
                    continue
                else:
                    res = False
                    break
            else:
                res = False
                break
        return res

class Db(Object):

    """ interface to objects stored on disk."""

    def all(self, otype, selector={}, index=None, delta=0):
        """all objects of a certain type."""
        nr = -1
        for fn in names(otype, delta):
            o = hook(fn)
            nr += 1
            if index is not None and nr != index:
                continue
            if selector and not o.search(selector):
                continue
            if "_deleted" in o and o._deleted:
                continue
            yield o

    def deleted(self, otype, selector={}):
        """deleted records of a type."""
        nr = -1
        for fn in names(otype):
            o = hook(fn)
            nr += 1
            if selector and not o.search(selector):
                continue
            if "_deleted" not in o or not o._deleted:
                continue
            yield o
        
    def find(self, otype, selector={}, index=None, delta=0):
        """match object based on a selector dict."""
        nr = -1
        for fn in names(otype, delta):
            o = hook(fn)
            if o.search(selector):
                nr += 1
                if index is not None and nr != index:
                    continue
                if "_deleted" in o and o._deleted:
                    continue
                yield o

    def find_value(self, otype, value, index=None, delta=0):
        """match objects based on stringified values.""" 
        nr = -1
        res = []
        for fn in names(otype, delta):
            o = hook(fn)
            if o.find(value):
                nr += 1
                if index is not None and nr != index:
                    continue
                if "_deleted" in o and o._deleted:
                    continue
                yield o

    def last(self, otype, index=None, delta=0):
        """last saved object of a type."""
        fns = names(otype, delta)
        if fns:
            fn = fns[-1]
            return hook(fn)

    def last_fn(self, otype, index=None, delta=0):
        """filename of the last object of a type."""
        fns = names(otype, delta)
        if fns:
            fn = fns[-1]
            return (fn, hook(fn))
        return (None, None)

    def last_all(self, otype, selector={}, index=None, delta=0):
        """reverser search."""
        nr = -1
        res = []
        for fn in names(otype, delta):
            o = hook(fn)
            if selector and o.search(selector):
                nr += 1
                if index is not None and nr != index:
                    continue
                res.append((fn, o))
            else:
                res.append((fn, o))
        if res:
            s = sorted(res, key=lambda x: fntime(x[0]))
            if s:
                return s[-1][-1]
        return None

class Default(Object):

    """provides the object with a default empty string value."""

    def __getattr__(self, k):
        if k not in self:
            self.__dict__.__setitem__(k, "")
        return self.__dict__[k]

class Cfg(Default):

    """configuration."""

    pass

cfg = Cfg()

class DoL(Object):

    """dict of lists."""

    def append(self, key, value):
        """add a value to the self[key] list."""
        if key not in dir(self):
            self[key] = []
        if type(value) == list:
            self[key].extend(value)
        else:
            self[key].append(value)

    def update(self, d):
        """custom update."""
        for k, v in d.items():
            self.append(k, v)

def cdir(path):
    """create a directory."""
    if os.path.exists(path):
        return
    res = ""
    path2, fn = os.path.split(path)
    for p in path2.split(os.sep):
        res += "%s%s" % (p, os.sep)
        padje = os.path.abspath(os.path.normpath(res))
        try:
            os.mkdir(padje)
        except (IsADirectoryError, NotADirectoryError, FileExistsError):
            pass
    return True

def fntime(daystr):
    """time in filename."""
    daystr = daystr.replace("_", ":")
    datestr = " ".join(daystr.split(os.sep)[-2:])
    try:
        datestr, rest = datestr.rsplit(".", 1)
    except ValueError:
        rest = ""
    try:
        t = time.mktime(time.strptime(datestr, "%Y-%m-%d %H:%M:%S"))
        if rest:
            t += float("." + rest)
    except ValueError:
        t = 0
    return t

def hd(*args):
    """homedir."""
    homedir = os.path.expanduser("~")
    return os.path.abspath(os.path.join(homedir, *args))

@locked(hooklock)
def hook(fn):
    """read file and convert it to an object."""
    #if fn in cache:
    #    return cache[fn]
    t = fn.split(os.sep)[0]
    if not t:
        t = fn.split(os.sep)[0][1:]
    if not t:
        raise ENOFILE(fn)
    o = lo.typ.get_cls(t)()
    o.load(fn)
    return o

def names(name, delta=None):
    """show all names in a directory."""
    assert workdir
    if not name:
        return []
    p = os.path.join(workdir, "store", name) + os.sep
    res = []
    now = time.time()
    if delta:
        past = now + delta
    for rootdir, dirs, files in os.walk(p, topdown=False):
        for fn in files:
            fnn = os.path.join(rootdir, fn).split(os.path.join(workdir, "store"))[-1]
            if delta:
                if fntime(fnn) < past:
                    continue
            res.append(os.sep.join(fnn.split(os.sep)[1:]))
    return sorted(res, key=fntime)
    #return list(reversed(sorted(res, key=fntime)))

def resulted(seq):
    """parse a result."""
    if seq == None:
        return []
    return list(reversed(sorted(seq, key=fntime)))
    
def stamp(o):
    """generate a path stamp in the object."""
    for k in dir(o):
        oo = getattr(o, k, None)
        if isinstance(oo, Object):
            stamp(oo)
            oo.__dict__["stamp"] = oo._path
            o[k] = oo
        else:
            continue
    o.__dict__["stamp"] = o._path
    return o

def strip(o, vals=["",]):
    """strip valued keys from an object."""
    rip = []
    for k in o:
        for v in vals:
            if k == v:
                rip.append(k)
    for k in rip:
        del o[k]
    return o

def touch(fname):
    """touch a file."""
    try:
        fd = os.open(fname, os.O_RDWR | os.O_CREAT)
        os.close(fd)
    except (IsADirectoryError, TypeError):
        pass

