#!/usr/bin/python3
"""
This module takes in the name of a state as an argument and lists all
cities of that state from the database hbtn_0e_4_usa.
The script is safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Validate that we have all 4 required arguments
    if len(sys.argv) >= 5:
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

        # Join cities and states to find cities belonging to the given state
        # Safe from SQL injection using %s as a placeholder
        query = "SELECT cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC"
        
        cur.execute(query, (sys.argv[4],))

        # Fetch all result rows
        rows = cur.fetchall()

        # Format output: join city names with commas
        # Example: Dallas, Houston, Austin
        print(", ".join([row[0] for row in rows]))

        # Clean up: close cursor and connection
        cur.close()
        db.close()
