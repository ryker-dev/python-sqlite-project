import sqlite3
import os

import band
import member
import members_in_bands as mib
import release
import track
import database

from database import sql_connect_to_db

DEBUG = True
PATH = os.path.dirname(__file__)

def print_menu():
    print("\n1: Add band")
    print("2: Add member")
    print("3: Add member to band")
    print("4: Add release")
    print("5: Add track\n")

    print("6: Print bands")
    print("7: Print members")
    print("8: Print band members")
    print("9: Print releases")
    print("10: Print tracks")
    print("0: Quit")

def user_menu():
    action = -1
    while(action != "0"):
        print_menu()
        action = input("Action: ")

        ##Inserts
        if action == "1":
            band.insert_band()
        if action == "2":
            member.insert_member()        
        if action == "3":
            mib.add_relation()
        if action == "4":
            release.insert_release()
        if action == "5":
            track.insert_track()

        ##Prints
        if action == "6":
            band.sql_print_bands()     
        if action == "7":
            member.sql_print_members()
        if action == "8":
            mib.sql_print_mib() 
        if action == "9":
            release.print_releases() 
        if action == "10":
            track.print_tracks() 

def main():
    database.create_db()
    user_menu()       
    return None

if __name__ == "__main__":
    main()