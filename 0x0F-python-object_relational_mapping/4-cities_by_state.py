#!/usr/bin/python3
'''Demonstrates how to work with MySQLdb'''
import MySQLdb
import sys


def listCities():
    '''Returns the lists of cities and states'''
    if len(sys.argv) < 4:
        sys.exit(f"Usage: {sys.argv[0]} user password database")
    user, pword, dbname = sys.argv[1:]
    db = None
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=user,
            passwd=pword,
            port=3306,
            db=dbname,
            charset='utf8',
            connect_timeout=5
            )
        query = f'''
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id
        '''
        with db.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
        for row in rows:
            print(row)
    except (MySQLdb.Error, MySQLdb.Warning, Exception) as msg:
        sys.exit(msg)
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    listCities()
