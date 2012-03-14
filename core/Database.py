import MySQLdb

from Error import HTTPException

class _DatabaseEngine:
    def __init__(self):
        self.conn = None
        self.cursor = None

class MySQLEngine(_DatabaseEngine):
    def __init__(self,host,user,passwd,db):
        self.conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db)
        self.cursor = self.conn.cursor()

#--------------------
import re
__cfg_file = open('CONFIG','r')
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
    else:
        raise HTTPException(500)

def DB():
    return _store.dbe
