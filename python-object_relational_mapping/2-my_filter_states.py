#!/usr/bin/python3
"""
This module takes an argument and displays all values in the states table
where name matches the argument provided by the user.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Ensure all 4 arguments are present: user, pass, db, and search name
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

        # Create cursor to execute queries
        cur = db.cursor()

        # Execute query using format() as requested by the task
        # Using BINARY to ensure exact match including case sensitivity
        query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
                 ORDER BY id ASC".format(state_name)
        cur.execute(query)

        # Fetch and print the results
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        # Close cursor and connection
        cur.close()
        db.close()
