from database import sql_connect_to_db

def add_relation():
    print("Inserting a member to a band")
    band_id = input("BAND ID: ") or None
    member_id = input("MEMBER ID: ") or None

    ## Add better input validation
    if (band_id is not None and member_id is not None):
        sql_add_relation(band_id, member_id)
        print("Member added to band!")

################ SQL FUNCTIONS ################

def sql_add_relation(band_id, member_id):
    db, cur = sql_connect_to_db()

    cur.execute('''
        INSERT INTO MembersInBands (bandID, memberID ) VALUES (?, ?)
    ''', (band_id, member_id))

    db.commit()
    db.close()

def sql_print_relations():
    db, cur = sql_connect_to_db()

    """ cur.execute("SELECT * FROM MembersInBands;") """
    cur.execute('''
        SELECT * FROM 
    ''')

    for item in cur.fetchall():
        print(item)
    
    db.close()