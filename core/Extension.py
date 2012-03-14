class _ExtMount(type):
    def __init__(cls,name,bases,attrs):
        if not hasattr(cls,'extensions'):
            cls.extensions = []
        else:
            cls.extensions.append(cls)

class BaseExtension:
    __metaclass__ = _ExtMount

Registry = []

def LoadExtensions():
    import ext
    for extclass in BaseExtension.extensions:
        Registry.append(extclass())
