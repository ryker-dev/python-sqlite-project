from database import sql_connect_to_db

################ SQL FUNCTIONS ################

## NOT IN USE
def sql_get_publisher_id(publisher_name):
    db, cur = sql_connect_to_db()

    cur.execute('''
        SELECT publisherID FROM Publisher
        WHERE ? = name;
    ''', (publisher_name,))

    name = cur.fetchone
    db.close()

    return len(name) < 1 and name or None