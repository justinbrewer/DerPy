from Extension import BaseExtension

class EventBuild(type):
    def __init__(cls,name,bases,attrs):
        cls.callback = 'on' + name

class Event:
    __metaclass__ = EventBuild

def DispatchEvent(e):
    handled = False
    for ext in BaseExtension.extensions:
        try:
            res = getattr(ext,e.callback)(e)
            if res == 1:
                handled = True
                continue
            elif res == 2:
                return True
        except:
            continue

    return handled
