class ExtMount(type):
    def __init__(cls,name,bases,attrs):
        if not hasattr(cls,'extensions'):
            cls.extensions = []
        else:
            cls.extensions.append(cls)
    
class BaseExtension:
    __metaclass__ = ExtMount

from ext import TestExtension
