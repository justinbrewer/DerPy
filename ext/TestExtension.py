from core.Extension import BaseExtension

class TestExtension(BaseExtension):
    desc = 'Derp'
    
    def onDerpEvent(self,e):
        print "Derp"
        return 1
