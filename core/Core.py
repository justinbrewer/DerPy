class Core:
    def __init__(self):
        self.http_code = '200 OK'
        self.output = ""
        self.headers = []
        
    def Run(self, env):
        self.output = "This needs to be about 20% cooler."
        self.headers = [('Content-type', 'text/html')]
        
        return
