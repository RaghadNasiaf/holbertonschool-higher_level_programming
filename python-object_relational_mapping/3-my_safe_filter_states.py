#!/usr/bin/python3
"""
This module provides a script that safely filters states by user input.
It prevents SQL injection by using parameterized queries with MySQLdb.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) >= 5:
        # Establish connection using command line arguments
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )

        # Create a cursor object for query execution
        cur = db.cursor()

        # Execute the query safely using the parameterized method
        # The tuple (sys.argv[4],) ensures the input is treated as data only
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                    (sys.argv[4],))

        # Fetch results and print each row
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        # Ensure cursor and connection are closed
        cur.close()
        db.close()
