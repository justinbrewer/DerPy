from Error import HTTPException

class DatabaseEngine:
    def __init__(self):
        self.conn = None
        self.cursor = None

class NullEngine(DatabaseEngine):
    def Close(self):
        pass

#--------------------
import re
__cfg_file = open('db.cfg','r')
__dsn = __cfg_file.readline().strip()
__cfg_file.close()
__conn_info = re.match(r"^(\w+)\:(?:user=(\w+)(?:;|$)|password=(\w+)(?:;|$)|host=([\w\.\-]+)(?:;|$)|dbname=([\w_]+)(?:;|$))+",__dsn)

_conn_info = list(__conn_info.groups())

del [__conn_info,__dsn,__cfg_file]

#--------------------
import threading
_store = threading.local()

def Connect():
    if _conn_info[0] == 'mysql':
        from drivers.MySQL import EngineImpl
        _store.dbe = EngineImpl(_conn_info[3],_conn_info[1],_conn_info[2],_conn_info[4])
    elif _conn_info[0] == 'null':
        _store.dbe = NullEngine()
    else:
        raise HTTPException(500)

def Disconnect():
    _store.dbe.Close()

def DB():
    return _store.dbe
