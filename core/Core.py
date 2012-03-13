from Event import DispatchEvent
from Error import HTTPErrorEvent, HTTPException
import Misc

class Core:
    def __init__(self):
        self.http_code = Misc.HTTPCode[200]
        self.output = []
        self.headers = []
        
    def Run(self, env):
        try:
            self.output = ["This needs to be about 20% cooler."]
            self.headers = [('Content-type', 'text/html')]
            
        except HTTPException as err:
            if err.fatal or not DispatchEvent(HTTPErrorEvent(err.code)):
                self.http_code = Misc.HTTPCode[err.code]
                self.headers = [('Content-type', 'text/html')]
                self.output = ['<h1>'+self.http_code+'</h1>']

        return

class OutputSegment:
    def __init__(self):
        self.data = []

    def __str__(self):
        return '\n'.join(self.data)

    def Add(self,i):
        self.data.append(i)

    def Key(self,k,v):
        for i in self.data:
            i = i % {k,v}
