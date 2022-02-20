import os
import names

from database import sql_connect_to_db

PATH = os.path.dirname(__file__)

def insert_band():
    print("Inserting a new band")
    print("(Enter to autogenerate name)")
    name = input("NAME: ")

    if (len(name) < 1):
        name = names.gen_band_name()

    date = input("date (YYYY/MM/DD): ") or None
    publisher_id = input("Publisher ID: ") or None

    ## Add better input validation

    sql_insert_band(name, publisher_id, date)
    print(name.capitalize() + " added!")

def gen_bands(amount):
    for i in range(amount):
        sql_insert_band(names.gen_band_name(), None, None) 


################ SQL FUNCTIONS ################

def sql_insert_band(name, publisher_id, date):
    db, cur = sql_connect_to_db()

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

    print("\nbandID | publisherID | name | creationDate | ")
    cur.execute("SELECT * FROM Band;")

    for item in cur.fetchall():
        print(item)
    
    db.close()