#!/usr/bin/python3
"""Import mysql and sys"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    sta = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(sta)
    cur.execute(
        query
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
