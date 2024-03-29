import Database
from Extension import LoadExtensions, UnloadExtensions
from Event import DispatchEvent, Event
from Error import HTTPErrorEvent, HTTPException

class OutputSegment:
    def __init__(self):
        self.data = []

    def __str__(self):
        return _Collapse(self.data)

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

#--------------------
import threading
_store = threading.local()

def Run(env):
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
        output.Add(['<html><head>',head,'</head><body>',body,'</body></html>'])
        
        return [_HTTPCode[response.code],response.GetHeaders(),[str(output)]]
    
    except HTTPException as err:
        if err.fatal or not DispatchEvent(HTTPErrorEvent(err.code)):
            return [_HTTPCode[err.code],[('Content-type', 'text/html')],['<h1>'+self.http_code+'</h1>']]

def Env():
    return _store.env

#--------------------
_HTTPCode = {200: '200 OK',
             302: '302 Found',
             403: '403 Forbidden',
             404: '404 Not Found',
             500: '500 Internal Server Error',
             503: '503 Service Unavailable'}

def _Collapse(data):
    flat = []
    for i in data:
        if isinstance(i,list):
            flat.append(_Collapse(i))
        else:
            flat.append(str(i))
    return '\n'.join(flat)
