import os
import random

from publisher import sql_get_publisher_id
from database import sql_connect_to_db

PATH = os.path.dirname(__file__)

def insert_member():
    print("Inserting a new member")
    print("(Enter to autogenerate name)")
    first = input("FIRST NAME: ") or None
    last = input("LAST NAME: ") or None

    if (first ==  None):
        first, last = gen_member_name()

    ## Add better input validation

    sql_insert_member(first, last)
    print("%s %s added!"%(first, last))

def gen_bands(amount):
    for i in range(0,amount):
        first, last = gen_member_name()
        sql_insert_member(first, last) 

def gen_member_name():
    first = random.choice( open(PATH + "/names/members/first.txt").read().splitlines())
    last = random.choice( open(PATH + "/names/members/last.txt").read().splitlines())
    
    return first, last

################ SQL FUNCTIONS ################

def sql_insert_member(first, last):
    db, cur = sql_connect_to_db()

    cur.execute('''
        INSERT INTO Member (firstName, lastName) VALUES (?, ?)
    ''', (first, last))
    db.commit()
    db.close()

def sql_print_members():
    db, cur = sql_connect_to_db()

    cur.execute("SELECT * FROM Member;")

    for item in cur.fetchall():
        print(item)
    
    db.close()