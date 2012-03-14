import Database
from Extension import LoadExtensions
from Event import DispatchEvent
from Error import HTTPErrorEvent, HTTPException

class Core:
    def __init__(self):
        self.http_code = _HTTPCode[200]
        self.output = []
        self.headers = []
        
    def Run(self, env):
        LoadExtensions()
        
        try:
            Database.Connect()
            
            self.output = ["This needs to be about 20% cooler."]
            self.headers = [('Content-type', 'text/html')]
            
        except HTTPException as err:
            if err.fatal or not DispatchEvent(HTTPErrorEvent(err.code)):
                self.http_code = _HTTPCode[err.code]
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

_HTTPCode = {200: '200 OK',
             302: '302 Found',
             403: '403 Forbidden',
             404: '404 Not Found',
             500: '500 Internal Server Error',
             503: '503 Service Unavailable'}
