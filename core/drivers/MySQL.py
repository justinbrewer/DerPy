import MySQLdb

from core.Database import DatabaseEngine

class EngineImpl(DatabaseEngine):
    def __init__(self,host,user,passwd,db):
        self.conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db)
        self.cursor = self.conn.cursor()
    
    def Close(self):
        self.conn.close()
