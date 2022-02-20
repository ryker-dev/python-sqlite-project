import os
import random
from database import sql_connect_to_db

PATH = os.path.dirname(__file__)

def insert_release():
    print("Inserting a new release")
    band_id = input("BAND ID: ")
    print("(Enter to autogenerate name)")
    name = input("RELEASE NAME: ") or None
    release_type = input("TYPE: ")
    date = input("DATE (YYYY/MM/DD): ")

    if name is None:
        name = gen_release_name()

    sql_insert_release(band_id, name, release_type, date)

def gen_release_name():
    name = random.choice(open(PATH + "/names/bands/wordlist.10000").read().splitlines())
    
    return name

def gen_releases(amount):
    for i in range(amount):
        sql_insert_release(None, gen_release_name(), None, None) 

def print_releases():
    band_id = input("BAND ID: ")
    sql_print_releases(band_id)

################ SQL FUNCTIONS ################

def sql_print_releases(band_id):
    db, cur = sql_connect_to_db()

    print("\nrealeaseID | bandID | name | type | date")
    cur.execute('''
        SELECT * FROM Release
        WHERE ? = bandID;
    ''', (band_id,))

    for item in cur.fetchall():
        print(item)
    
    db.close()

def sql_insert_release(band_id, name, release_type, date):
    db, cur = sql_connect_to_db()

    cur.execute('''
        INSERT INTO Release (bandID, name, type, date) VALUES (?, ?, ?, ?)
    ''', (band_id, name, release_type, date))

    db.commit()
    db.close()