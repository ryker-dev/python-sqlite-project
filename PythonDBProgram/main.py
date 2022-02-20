import os

import band
import member
import members_in_bands as mib
import release
import track
import database
import review
import bokeh_charts as bk

from database import sql_connect_to_db

PATH = os.path.dirname(__file__)

def print_menu():
    print("\n1: Add band")
    print("2: Add member")
    print("3: Add member to band")
    print("4: Add release")
    print("5: Add track")
    print("6: Add review\n")

    print("7: Print bands")
    print("8: Print members")
    print("9: Print band members")
    print("10: Print releases")
    print("11: Print tracks")
    print("12: Print reviews")
    print("0: Quit")

def user_menu():
    action = -1
    while(action != "0"):
        print_menu()
        action = input("Action: ")

        if action == "0":
            return

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
        if action == "6":
            review.insert_review()

        ##Prints
        if action == "7":
            band.sql_print_bands()     
        if action == "8":
            member.sql_print_members()
        if action == "9":
            mib.sql_print_mib() 
        if action == "10":
            release.print_releases() 
        if action == "11":
            track.print_tracks() 
        if action == "12":
            review.print_reviews()

        input("Press enter to continue")

def main():
    database.create_db()
    bk.bk_band_releases()
    ''' user_menu()  '''      
    return None

if __name__ == "__main__":
    main()