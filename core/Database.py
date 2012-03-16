import MySQLdb

from Error import HTTPException

class _DatabaseEngine:
    def __init__(self):
        self.conn = None
        self.cursor = None

class NullEngine(_DatabaseEngine):
    def Close(self):
        pass

class MySQLEngine(_DatabaseEngine):
    def __init__(self,host,user,passwd,db):
        self.conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db)
        self.cursor = self.conn.cursor()
    
    def Close(self):
        self.conn.close()

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
        _store.dbe = MySQLEngine(_conn_info[3],_conn_info[1],_conn_info[2],_conn_info[4])
    elif _conn_info[0] == 'null':
        _store.dbe = NullEngine()
    else:
        raise HTTPException(500)

def Disconnect():
    _store.dbe.Close()

def DB():
    return _store.dbe
