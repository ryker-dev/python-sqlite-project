import sqlite3
import os.path

PATH = os.path.dirname(__file__)

def create_db():
    
    db, cur = sql_connect_to_db()

    try:
        f = open(PATH + "/../SQL queries.sql", "r") ## Execution method taken from Topic 6: Python
        commands = ""
        for line in f.readlines():
            commands+=line
        cur.executescript(commands)
        print("No database detected. Database initialised")
    except sqlite3.OperationalError as err:
        print(err)
    except Exception as err:
        print(err)
    db.close()

def sql_connect_to_db():
    db = sqlite3.connect(PATH + "/db/db.sqlite")
    cur = db.cursor()
    
    return db, cur