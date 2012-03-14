from sys import maxint

class _ExtMount(type):
    def __init__(cls,name,bases,attrs):
        if not hasattr(cls,'extensions'):
            cls.extensions = []
        else:
            cls.extensions.append(cls)
            print name

class StaticExtension:
    __metaclass__ = _ExtMount
    priority = maxint

class BaseExtension:
    __metaclass__ = _ExtMount
    priority = maxint

def _Key(e):
    try:
        return getattr(e,'priority')
    except AttributeError:
        return maxint

#--------------------
import ext
_StaticRegistry = []

for extclass in StaticExtension.extensions:
    _StaticRegistry.append(extclass())
_StaticRegistry.sort(key=_Key)

#--------------------
import threading
_store = threading.local()

def LoadExtensions():
    _store.registry = []
    for extclass in BaseExtension.extensions:
        _store.registry.append(extclass())
    _store.registry.extend(_StaticRegistry)
    _store.registry.sort(key=_Key)

def GetExtensions():
    try:
        return _store.registry
    except AttributeError:
        return _StaticRegistry
