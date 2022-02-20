import os
import random

from publisher import sql_get_publisher_id
from database import sql_connect_to_db

PATH = os.path.dirname(__file__)

def insert_band():
    print("Inserting a new band")
    print("(Enter to autogenerate name)")
    name = input("NAME: ")

    if (len(name) < 1):
        name = gen_band_name()

    date = input("date (YYYY/MM/DD): ") or None
    publisher = input("Publisher: ") or None

    ## Add better input validation

    sql_insert_band(name, publisher, date)
    print(name.capitalize() + " added!")

def gen_bands(amount):
    for i in range(0,amount):
        sql_insert_band(gen_band_name(), None, None) 

def gen_band_name():
    words = open(PATH + "/names/bands/wordlist.10000").read().splitlines()
    name = "%s %s"%(random.choice(words), random.choice(words))
    
    return name

################ SQL FUNCTIONS ################

def sql_insert_band(name, publisher, date):
    db, cur = sql_connect_to_db()

    if (not publisher == None):
        publisher_id = sql_get_publisher_id(publisher)
    else:
        publisher_id = None

    cur.execute('''
        INSERT INTO Band (name, publisherID, creationDate) VALUES (?, ?, ?)
    ''', (name, publisher_id, date))
    db.commit()
    db.close()

def sql_get_band_id(band_name):
    db, cur = sql_connect_to_db()

    cur.execute('''
        SELECT bandID FROM Band
        WHERE ? = name;
    ''', (band_name,))

    name = cur.fetchone
    db.close()

    return len(name) < 1 and name or None

def sql_print_bands():
    db, cur = sql_connect_to_db()

    cur.execute("SELECT * FROM Band;")

    for item in cur.fetchall():
        print(item)
    
    db.close()