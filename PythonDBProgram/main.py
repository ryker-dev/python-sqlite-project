import sqlite3
import os

from bands import *
from database import *

from django.template import VariableDoesNotExist

DEBUG = True
PATH = os.path.dirname(__file__)

def create_db():

    db, cur = connect_to_db()

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
    print("0: Quit")

def user_menu():
    action = -1
    while(action != "0"):
        print_menu()
        action = input("Action: ")

        if action == "1":
            insert_band()

def main():
    create_db()
    user_menu()       
    return None

if __name__ == "__main__":
    main()