#!/usr/bin/python3
'''Demonstrates working with MySQLdb'''
import sys
import MySQLdb


def filter():
    '''Takes in the username and password of mysql, the database name
    and the filter. It returns all the names of states starting with the
    filter specified'''
    argv = sys.argv[1:]
    db = None
    if len(argv) < 4:
        sys.exit(f"Usage {sys.argv[0]} username password database filter")
    user, pword, dbname, fstr = argv
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
        sqlquery = '''
            SELECT *
            FROM states
            WHERE states.name
            LIKE '{}%'
            ORDER BY states.id
            '''.format(fstr)
        with db.cursor() as cur:
            cur.execute(sqlquery)
            rows = cur.fetchall()
        for row in rows:
            print(row)
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        sys.exit(e)
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    filter()
