import sqlite3

class Connection(object): 
    @staticmethod
    def Connect():
        try:
            conn = sqlite3.connect('db.sqlite3')
            return conn
        except:
            return null