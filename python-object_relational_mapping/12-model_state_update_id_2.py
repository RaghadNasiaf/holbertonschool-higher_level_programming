#!/usr/bin/python3
"""
This module changes the name of a State object from the database hbtn_0e_6_usa.
It specifically updates the state with id = 2 to 'New Mexico'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Check if all 3 required arguments are provided
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

        # Query the specific state where id is 2
        state_to_update = session.query(State).filter(State.id == 2).first()

        # If the state exists, update its name and commit the changes
        if state_to_update:
            state_to_update.name = "New Mexico"
            session.commit()

        # Close the session properly
        session.close()
