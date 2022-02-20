import sqlite3
import os

import database
import menu

DEBUG = True
PATH = os.path.dirname(__file__)

def create_db():

    db, cur = database.sql_connect_to_db()

    try:
        f = open(PATH + "/../SQL queries.sql", "r") ## Execution method taken from Topic 6: Python
        commands = ""
        for line in f.readlines():
            commands+=line
        cur.executescript(commands)
    except sqlite3.OperationalError:
        print("Database already exists, skipping")
    except Exception as err:
        print(err)
    db.close()

def main():
    create_db()
    menu.menu_handler()       
    return None

if __name__ == "__main__":
    main()