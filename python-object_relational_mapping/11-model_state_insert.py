#!/usr/bin/python3
"""
This module adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
It prints the new state's id after creation.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Ensure all 3 required arguments are present
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

        # Create a new State object
        new_state = State(name="Louisiana")

        # Add the new state to the session and commit to save it
        session.add(new_state)
        session.commit()

        # Print the new state's id
        print("{}".format(new_state.id))

        # Close the session properly
        session.close()
