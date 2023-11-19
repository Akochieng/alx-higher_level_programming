#!/usr/bin/python3
'''Demonstrates working with MySQLdb'''
import sys
import MySQLdb


def filter():
    '''Prints states whose names starts with the specified letters
    while protecting against SQL injection'''
    argv = sys.argv[1:]
    if len(argv) < 4:
        sys.exit(f"Usage {sys.argv[0]} username password database filter")
    user, pword, dbname, fstr = argv
    db = None
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
        query = f'''SELECT *
                FROM states
                WHERE states.name
                LIKE %s
                ORDER BY states.id
                '''
        with db.cursor() as cur:
            cur.execute(query, (fstr,))
            rows = cur.fetchall()
        for row in rows:
            print(row)
    except (MySQLdb.Error, MySQLdb.Warning, Exception) as e:
        print(e)
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    filter()
