#!/usr/bin/python3
"""
This module provides a script that lists all states from the database.
The script connects to a MySQL server and fetches data from hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) >= 4:
        db_user = sys.argv[1]
        db_pass = sys.argv[2]
        db_name = sys.argv[3]

        # Initialize connection to the database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=db_user,
            passwd=db_pass,
            db=db_name,
            charset="utf8"
        )

        # Create a cursor object for query execution
        cur = db.cursor()

        # Execute the selection query ordered by states.id
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch and print each row from the result set
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        # Ensure cursor and connection are closed properly
        cur.close()
        db.close()
