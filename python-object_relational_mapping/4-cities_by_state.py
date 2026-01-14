#!/usr/bin/python3
"""
This module lists all cities from the database hbtn_0e_4_usa.
The script uses a JOIN to combine data from cities and states tables.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Validate arguments length
    if len(sys.argv) >= 4:
        # Establish connection to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )

        # Create a cursor object
        cur = db.cursor()

        # Execute a JOIN query to fetch city id, city name, and state name
        # Sorted by cities.id in ascending order
        cur.execute("SELECT cities.id, cities.name, states.name \
                     FROM cities \
                     JOIN states ON cities.state_id = states.id \
                     ORDER BY cities.id ASC")

        # Fetch and print results
        rows = cur.fetchall()
        for row in rows:
            print(row)

        # Close cursor and database connection
        cur.close()
        db.close()
