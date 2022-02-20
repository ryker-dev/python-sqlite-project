import band
import member
import members_in_bands as mib
import release

def display_menu_dict():
    return {
        1: "Print bands",
        2: "Print members",
        3: "Print band members",
        4: "Print releases",
        5: "<- Previous"
    }

def insertion_menu_dict():
    return {
        1: "Add bands",
        2: "Add members",
        3: "Add band members",
        4: "Add releases",
        5: "<- Previous"
    }

def main_menu_dict():
    return {
        1: "Add entries",
        2: "Print entries"
    }

def print_menu(type):
    menu = {
        "main": main_menu_dict(),
        "print": display_menu_dict(),
        "insert": insertion_menu_dict()
    }

    print("\n")
    print(menu.keys("main"))
    for i in menu[type]:
        print(i, menu[i])

    print("0: Quit")

def menu_handler():
    action = -1
    while action:
        print_menu("main")
        action = input("Action: ")

        if (action == 1):
            print_menu("insert")
            action = input("Action: ")

            if action == "1":
                band.insert_band()
            if action == "2":
                member.insert_member()        
            if action == "3":
                mib.add_relation()
            if action == "4":
                release.insert_release()

        elif (action == 2):
            print_menu("print")
            action = input("Action: ")
            if action == "1":
                band.sql_print_bands()     
            if action == "2":
                member.sql_print_members()
            if action == "3":
                mib.sql_print_mib() 
            if action == "4":
                release.print_releases() 
        else: return