#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Establishing connection to the database using command line arguments
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Creating a cursor object to execute SQL commands
    cur = db.cursor()

    # Executing the JOIN query to fetch city names based on state name
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (sys.argv[4],))

    # Fetching all results and joining them into a comma-separated string
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    # Closing all connections properly
    cur.close()
    db.close()
