from Extension import BaseExtension

class EventBuild(type):
    def __init__(cls,name,bases,attrs):
        cls.callback = 'on' + name

class Event:
    __metaclass__ = EventBuild

def DispatchEvent(e):
    handled = 0
    for ext in BaseExtension.extensions:
        try:
            res = getattr(ext,e.callback)(e)
            if res == 1:
                handled = 1
                continue
            elif res == 2:
                return 2
        except:
            continue

    return handled
