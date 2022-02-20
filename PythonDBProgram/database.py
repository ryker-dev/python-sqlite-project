import sqlite3
import os.path

def connect_to_db():
    db = sqlite3.connect(os.path.dirname(__file__) + "/db/db.sqlite")
    cur = db.cursor()
    
    return db, cur