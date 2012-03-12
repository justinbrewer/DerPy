from Event import Event

class HTTPErrorEvent(Event):
    def __init__(self, code):
        self.code = code

class HTTPException(Exception):
    def __init__(self,code=500,fatal=False):
        self.code = code
        self.fatal = fatal
