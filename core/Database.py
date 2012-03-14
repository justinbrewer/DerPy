import MySQLdb
import re

from Config import DSN
from Error import HTTPException

DB = None

def Connect():
    conn_info = re.match(r"^(\w+)\:(?:user=(\w+)(?:;|$)|password=(\w+)(?:;|$)|host=([\w\.\-]+)(?:;|$)|dbname=([\w_]+)(?:;|$))+",DSN)
    proto,user,password,host,dbname = conn_info.groups()
    
    if proto == 'mysql':
        DB = MySQLEngine(host,user,password,dbname)
    else:
        raise HTTPException(500)

class _DatabaseEngine:
    def __init__(self):
        self.conn = None
        self.cursor = None

class MySQLEngine(_DatabaseEngine):
    def __init__(self,host,user,passwd,db):
        self.conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db)
        self.cursor = self.conn.cursor()