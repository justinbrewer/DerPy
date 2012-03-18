import MySQLdb

from core.Database import DatabaseEngine

class EngineImpl(DatabaseEngine):
    def __init__(self,**kwargs):
        self.conn = MySQLdb.connect(**kwargs)
        self.cursor = self.conn.cursor()
    
    def Close(self):
        self.conn.close()
