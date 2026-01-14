#!/usr/bin/python3
"""
This module lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
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

        # Query State objects containing the letter 'a'
        # Sorted by id in ascending order
        states = session.query(State).filter(State.name.contains('a'))\
                                     .order_by(State.id).all()

        # Display results in the format: id: name
        for state in states:
            print("{}: {}".format(state.id, state.name))

        # Close the session properly
        session.close()
