#!/usr/bin/python3
"""
This module deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Ensure all 3 required arguments are provided
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

        # Query all states containing the letter 'a'
        states_to_delete = session.query(State).filter(
            State.name.contains('a')
        ).all()

        # Delete each state found and commit the changes
        for state in states_to_delete:
            session.delete(state)
        
        session.commit()

        # Close the session properly
        session.close()
