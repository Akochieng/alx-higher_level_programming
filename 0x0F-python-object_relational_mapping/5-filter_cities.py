#!/usr/bin/python3
'''Demonstrates how to work with MySQLdb'''
import MySQLdb
import sys


def listCities():
    '''Displays the cities in the specified state'''
    if len(sys.argv) < 5:
        sys.exit(f"Usage: {sys.argv[0]} user password database state")
    user, pword, dbname, state = sys.argv[1:]
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
        SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
        '''
        with db.cursor() as cur:
            cur.execute(query, (state,))
            rows = cur.fetchall()
        for index, row in enumerate(rows):
            for val in row:
                print(val, end='')
            if index == len(rows) - 1:
                print('')
            else:
                print(', ', end='')
    except (MySQLdb.Error, MySQLdb.Warning, Exception) as msg:
        sys.exit(msg)
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    listCities()
