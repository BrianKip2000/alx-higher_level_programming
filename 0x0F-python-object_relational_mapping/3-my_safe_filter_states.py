#!/usr/bin/python3
"""Import mysqldb and sys"""
import MySQLdb as ms
import sys

if __name__ == "__main__":
    usrname = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = ms.connect(
        host='localhost',
        port=3306,
        user=usrname,
        passwd=password,
        db=dbname
        )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
