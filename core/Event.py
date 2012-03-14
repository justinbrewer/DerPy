from Extension import GetExtensions

class _EventBuild(type):
    def __init__(cls,name,bases,attrs):
        cls.callback = 'on' + name

class Event:
    __metaclass__ = _EventBuild

def DispatchEvent(e):
    extensions = GetExtensions()
    handled = False
    for ext in extensions:
        try:
            cb = getattr(ext,e.callback)
        except:
            continue

        res = cb(e)
        if res == 1:
            handled = True
            continue
        elif res == 2:
            return True

    return handled
