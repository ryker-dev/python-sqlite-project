import sqlite3
import os
import random

DEBUG = True
PATH = os.path.dirname(__file__)

db = sqlite3.connect(PATH + "/db/db.sqlite")
cur = db.cursor()

def create_db():
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

def add_band(name, date):
    db.execute('''
        INSERT INTO Band (name, creation_date) VALUES (?, ?)
    ''', (name, date))
    db.commit()

def gen_bands(amount):
    if not DEBUG:
        return
    for i in range(0,amount):
        add_band(gen_band_name(), None) 

def gen_band_name():
    words = open(PATH + "/../devdoc/wordlist.10000").read().splitlines()
    name = "%s %s"%(random.choice(words), random.choice(words))
    
    return name
        
def main():
    create_db()
    gen_bands(10)
    db.close()        
    return None

if __name__ == "__main__":
    main()