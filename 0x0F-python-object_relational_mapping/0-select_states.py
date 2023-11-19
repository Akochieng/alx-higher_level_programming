#!/usr/bin/python3
'''Demonstrates how to work with the MySQLdb module'''
import sys
import MySQLdb


def func():
    '''Accepts the user name, password and name of the database and
    returns the list of states in the table states'''
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
            ORDER BY states.id
            ''')
        rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == '__main__':
    func()
