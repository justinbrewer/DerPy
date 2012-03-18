import Database
from Extension import LoadExtensions, UnloadExtensions
from Event import DispatchEvent, Event
from Error import HTTPErrorEvent, HTTPException

class Core:
    def __init__(self):
        self.http_code = _HTTPCode[200]
        self.output = []
        self.headers = []
        
    def Run(self, env):
        try:
            _store.env = env
            
            Database.Connect()
            LoadExtensions()
            
            DispatchEvent(PageRequestEvent(env['PATH_INFO']))
            
            response = ResponseBuildEvent()
            DispatchEvent(response)

            head = HeadBuildEvent()
            DispatchEvent(head)
            
            body = BodyBuildEvent()
            DispatchEvent(body)
            
            UnloadExtensions()
            Database.Disconnect()
            
            output = OutputSegment()
            output.Add('<html><head>')
            output.Add(head)
            output.Add('</head><body>')
            output.Add(body)
            output.Add('</body></html>')
            
            self.http_code = _HTTPCode[response.GetCode()]
            self.headers = response.GetHeaders()
            self.output = [str(output)]
            
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
        return '\n'.join(map(str,self.data))

    def Add(self,i):
        self.data.append(i)

    def Key(self,k,v):
        for i in self.data:
            i = i % {k,v}

class PageRequestEvent(Event):
    def __init__(self,path):
        self.path = path

class ResponseBuildEvent(Event):
    def __init__(self):
        self.code = 200
        self.headers = {'Content-type':'text/html'}
    
    def SetCode(self,i):
        self.code = i
    
    def GetCode(self):
        return self.code
    
    def SetHeader(self,k,v):
        self.headers[k] = v
    
    def GetHeaders(self):
        return self.headers.items()

class HeadBuildEvent(OutputSegment,Event):
    def __init__(self):
        super(HeadBuildEvent,self).__init__()

class BodyBuildEvent(OutputSegment,Event):
    def __init__(self):
        super(BodyBuildEvent,self).__init__()

_HTTPCode = {200: '200 OK',
             302: '302 Found',
             403: '403 Forbidden',
             404: '404 Not Found',
             500: '500 Internal Server Error',
             503: '503 Service Unavailable'}

#--------------------
import threading
_store = threading.local()

def Env():
    return _store.env
