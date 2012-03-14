from core.Extension import BaseExtension, StaticExtension

class DerpExtension(BaseExtension):
    desc = 'Derp'
    
    def __init__(self):
        print 'Derp'
    
    def onDerpEvent(self,e):
        print "Derp"
        return 1

class HerpExtension(StaticExtension):
    def __init__(self):
        print 'Herp'
