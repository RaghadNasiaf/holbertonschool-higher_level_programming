#!/usr/bin/python3
"""
This module prints the first State object from the database hbtn_0e_6_usa.
If the table is empty, it prints 'Nothing'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Access command line arguments for the database connection
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]

        # Create engine to connect to the MySQL server
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(user, passwd, db_name),
                               pool_pre_ping=True)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the first state object ordered by its ID
        # .first() is used to fetch only one record efficiently
        first_state = session.query(State).order_by(State.id).first()

        # Check if a state was found or the table is empty
        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        # Close the session properly
        session.close()
