#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
The script takes 3 arguments: mysql username, mysql password and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Access command line arguments
    if len(sys.argv) >= 4:
        db_user = sys.argv[1]
        db_pass = sys.argv[2]
        db_name = sys.argv[3]

        # Connect to a MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=db_user,
            passwd=db_pass,
            db=db_name,
            charset="utf8"
        )

        # Create a cursor object to execute SQL queries
        cur = db.cursor()
        
        # Execute the query to get all states ordered by id
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all results and print them as requested
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

        # Close cursor and database connection
        cur.close()
        db.close()
