from Error import HTTPException

class DatabaseEngine:
    def __init__(self):
        self.conn = None
        self.cursor = None

class NullEngine(DatabaseEngine):
    def __init__(self,**kwargs):
        pass
    def Close(self):
        pass

#--------------------
import re
__cfg_file = open('db.cfg','r')
__dsn = __cfg_file.readline().strip()
__cfg_file.close()
__conn_info = re.match(r"^(?P<proto>\w+)\:(?:user=(?P<user>\w+)(?:;|$)|password=(?P<passwd>\w+)(?:;|$)|host=(?P<host>[\w\.\-]+)(?:;|$)|dbname=(?P<db>[\w_]+)(?:;|$))+",__dsn)

_conn_info = __conn_info.groupdict()

del [__conn_info,__dsn,__cfg_file]

#--------------------
import threading
_store = threading.local()

def Connect():
    if _conn_info['proto'] == 'mysql':
        from drivers.MySQL import EngineImpl
    elif _conn_info['proto'] == 'null':
        class EngineImpl(NullEngine): pass
    else:
        raise HTTPException(500)
    
    _store.dbe = EngineImpl(**_conn_info.copy())

def Disconnect():
    _store.dbe.Close()

def DB():
    return _store.dbe
