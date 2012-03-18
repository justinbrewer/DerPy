try:
    from mod_wsgi import version
    import sys
    import os
    os.chdir(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(__file__))
except:
    raise
    
from core.Core import Run

def application(environment, response_callback):
    res = Run(environment)
    
    response_callback(res[0], res[1])
    return res[2]
