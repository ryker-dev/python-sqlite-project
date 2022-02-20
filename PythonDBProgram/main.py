import sqlite3
import os

import band
import member
import members_in_bands as mib
import release

from database import sql_connect_to_db

DEBUG = True
PATH = os.path.dirname(__file__)

def create_db():

    db, cur = sql_connect_to_db()

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

def print_menu():
    print("\n1: Add band")
    print("2: Add member")
    print("3: Add member to band")
    print("4: Add release\n")

    print("5: Print bands")
    print("6: Print members")
    print("7: Print band members")
    print("8: Print releases")
    print("0: Quit")

def user_menu():
    action = -1
    while(action != "0"):
        print_menu()
        action = input("Action: ")

        if action == "1":
            band.insert_band()
        if action == "2":
            member.insert_member()        
        if action == "3":
            mib.add_relation()
        if action == "4":
            release.insert_release()
        if action == "5":
            band.sql_print_bands()     
        if action == "6":
            member.sql_print_members()
        if action == "7":
            mib.sql_print_mib() 
        if action == "8":
            release.print_releases() 

def main():
    create_db()
    user_menu()       
    return None

if __name__ == "__main__":
    main()