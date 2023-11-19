#!/usr/bin/python3
'''Demonstrates working with MySQLdb'''
import sys
import MySQLdb


def filter():
    '''Takes in the username and password to mysql and the database name
    as arguments and returns the names of states starting with N'''
    argv = sys.argv[1:]
    if len(argv) < 3:
        sys.exit(f"Usage {sys.argv[0]} username password database")
    user, pword, dbname = argv
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=pword,
            db=dbname,
            charset='utf8',
            connect_timeout=5
            )
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        sys.exit(e)
    with db.cursor() as cur:
        cur.execute('''
        SELECT *
        FROM states
        WHERE states.name
        LIKE 'N%'
        ORDER BY states.id
        ''')
        rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == '__main__':
    filter()
