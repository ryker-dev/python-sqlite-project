from database import sql_connect_to_db
import names
import random

def print_reviews():
    release_id = input("RELEASE ID: ")
    sql_print_reviews(release_id)

def insert_review():
    print("Inserting a new review")
    release_id = input("RELEASE ID: ")
    print("(Enter to autogenerate name)")
    first = input("FIRST NAME:") or None
    last = input("LAST NAME:") or None
    content = input("CONTENT: ")

    if (first ==  None):
        first, last = names.gen_member_name()

    sql_insert_review(release_id, first, last, content)
    print("Review by %s %s added!"%(first, last))

def gen_reviews(amount):
    reviews = ["Was very good!", "Loved it!", "Wasn't very good", "Hate it", "Meh", "Didn't really like it", "Would have preferred something else"]
    for i in range(0,amount):
        first, last = names.gen_member_name()
        sql_insert_review(None, first, last, random.choice(reviews)) 

################ SQL FUNCTIONS ################

def sql_insert_review(release_id, first, last, content):
    db, cur = sql_connect_to_db()

    cur.execute('''
        INSERT INTO ReleaseReview (releaseID, firstName, lastName, content) VALUES (?, ?, ?, ?)
    ''', (release_id, first, last, content))

    db.commit()
    db.close()

def sql_print_reviews(release_id):
    db, cur = sql_connect_to_db()

    cur.execute('''
        SELECT * FROM ReleaseReview
        WHERE ? = releaseID;
    ''', (release_id,))

    for item in cur.fetchall():
        print(item)

    db.close()