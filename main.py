import sys
import os
sys.path.append(os.path.dirname(__file__))

from core.Core import Core

def application(environment, response_callback):
    c = Core()
    c.Run(environment)
    
    response_callback(c.http_code, c.headers)
    return [c.output]
