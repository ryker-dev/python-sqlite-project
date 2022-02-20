from database import *


def sql_get_publisher_id(publisher_name):
    db, cur = connect_to_db()

    db.execute('''
        SELECT name FROM Publisher
        WHERE ? = publisherID;
    ''', (publisher_name,))

    name = cur.fetchone
    db.close()

    return len(name) < 1 and name or None