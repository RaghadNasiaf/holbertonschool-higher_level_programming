#!/usr/bin/python3
"""
This module defines a script that lists all cities of a given state.
It uses MySQLdb to safely query the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Access command line arguments for database connection and search
    if len(sys.argv) >= 5:
        # Establish a secure connection to the database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )

        # Create a cursor object for executing SQL joins
        cur = db.cursor()

        # Execute query with JOIN and parameterized WHERE clause for safety
        query = "SELECT cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC"

        cur.execute(query, (sys.argv[4],))

        # Fetch all resulting city names and format them as a string
        rows = cur.fetchall()
        
        # Use join to display cities separated by a comma and a space
        print(", ".join([row[0] for row in rows]))

        # Close all resources
        cur.close()
        db.close()
