from Extension import LoadExtensions
import Misc

class Core:
    def __init__(self):
        self.http_code = Misc.HTTPCode['200']
        self.output = []
        self.headers = []
        
    def Run(self, env):
        LoadExtensions()
        
        self.output = ["This needs to be about 20% cooler."]
        self.headers = [('Content-type', 'text/html')]
        
        return
