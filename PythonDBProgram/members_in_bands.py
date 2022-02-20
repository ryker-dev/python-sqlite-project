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

def sql_print_mib():
    db, cur = sql_connect_to_db()

    """ cur.execute("SELECT * FROM MembersInBands;") """

    print("\nBand | Member")
    cur.execute('''
        SELECT Band.name, COALESCE(Member.firstName, '') || COALESCE(" ", '') ||COALESCE(Member.lastName, '') AS memberName FROM Band
        INNER JOIN MembersInBands ON Band.bandID = MembersInBands.bandID
        INNER JOIN Member ON MembersInBands.memberID = Member.memberID
        GROUP BY name, firstName;
    ''')

    for item in cur.fetchall():
        print(item)
    
    
    db.close()