#!/usr/bin/python3
"""Importing modules of sys and mysql"""
import sys
import MySQLdb

if __name__ == "__main__":
    """Takes in db name, password, mysql username"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            password=mysql_password,
            db=database_name
            )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
