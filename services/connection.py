import sqlite3
import os

class ConnectionFactory:
    _base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database'))
    _database = os.path.join(_base_dir, 'database.sqlite3')
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            try:
                cls._connection = sqlite3.connect(cls._database)
                cls._connection.row_factory = sqlite3.Row
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")
                return None
        return cls._connection

    @classmethod
    def get_cursor(cls):
        conn = cls.get_connection()
        return conn.cursor() if conn else None

    @classmethod
    def close_connection(cls):
        if cls._connection:
            cls._connection.close()
            cls._connection = None
