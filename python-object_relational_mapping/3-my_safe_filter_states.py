#!/usr/bin/python3
"""
This module lists all values in the states table where name matches the argument.
This script is safe from MySQL injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) >= 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object for query execution
        cur = db.cursor()

        # Safely execute query using parameterized input to prevent SQL injection
        # Use a tuple (state_name,) to pass the argument safely
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        # Fetch results and print them
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        # Close cursor and database connection
        cur.close()
        db.close()
