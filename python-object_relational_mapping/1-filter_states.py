#!/usr/bin/python3
"""
This module filters and lists all states starting with 'N' from the database.
The script takes 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get database credentials from command line arguments
    if len(sys.argv) >= 4:
        db_user = sys.argv[1]
        db_pass = sys.argv[2]
        db_name = sys.argv[3]

        # Establish connection to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=db_user,
            passwd=db_pass,
            db=db_name,
            charset="utf8"
        )

        # Create a cursor object to execute SQL commands
        cur = db.cursor()

        # Execute query to fetch states starting with uppercase N
        # ORDER BY id in ascending order
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                     ORDER BY states.id ASC")

        # Fetch all results and print each row
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        # Clean up: close cursor and connection
        cur.close()
        db.close()
