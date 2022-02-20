import os
from platform import release
import random
from database import sql_connect_to_db

PATH = os.path.dirname(__file__)

def insert_release():
    print("Inserting a new track")
    release_id = input("RELEASE ID: ") or None
    print("(Enter to autogenerate name)")
    name = input("TRACK NAME: ") or None
    length = input("LENGTH (seconds): ")

    if release_id is None:
        print("Invalid release ID")
        return
    if name is None:
        name = gen_track_name()

    sql_insert_track(release_id, name, length)

def gen_track_name():
    name = random.choice(open(PATH + "/names/bands/wordlist.10000").read().splitlines())
    
    return name

def gen_tracks(amount):
    for i in range(amount):
        sql_insert_track(None, gen_track_name(), None) 

def print_tracks():
    release_id = input("RELEASE ID: ")
    sql_print_tracks(release_id)

################ SQL FUNCTIONS ################

def sql_print_tracks(release_id):
    db, cur = sql_connect_to_db()

    cur.execute('''
        SELECT name, type FROM Track
        WHERE ? = releaseID;
    ''', (release_id,))

    for item in cur.fetchall():
        print(item)
    
    db.close()

def sql_insert_track(release_id, name, length):
    db, cur = sql_connect_to_db()

    cur.execute('''
        INSERT INTO Track (releaseID, name, length) VALUES (?, ?, ?)
    ''', (release_id, name, length))

    db.commit()
    db.close()