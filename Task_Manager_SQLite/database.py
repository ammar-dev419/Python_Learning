import sqlite3
import os

class Database:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.connection = sqlite3.connect(os.path.join(BASE_DIR, "tasks.db"))
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()