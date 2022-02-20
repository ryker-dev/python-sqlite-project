import os
import random

from publisher import *
from database import *

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
    print("Band added!")

def gen_bands(amount):
    for i in range(0,amount):
        sql_insert_band(gen_band_name(), None, None) 

def gen_band_name():
    words = open(PATH + "/../devdoc/wordlist.10000").read().splitlines()
    name = "%s %s"%(random.choice(words), random.choice(words))
    
    return name

################ SQL FUNCTIONS ################

def sql_insert_band(name, publisher, date):
    db, cur = connect_to_db()

    if (not publisher == None):
        publisher_id = sql_get_publisher_id(publisher)
    else:
        publisher_id = None

    db.execute('''
        INSERT INTO Band (name, publisherID, creation_date) VALUES (?, ?, ?)
    ''', (name, publisher_id, date))
    db.commit()
    db.close()