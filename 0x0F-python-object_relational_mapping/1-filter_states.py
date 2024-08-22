#!/usr/bin/python3
"""Script that lists all states from the database with names ending in 'N'."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments: mysql username, mysql password, and database name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute SQL query to select states with names ending in 'N', sorted by id
    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )

    # Fetch all the rows from the executed query
    rows = cur.fetchall()

    # Print each row in the result
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
