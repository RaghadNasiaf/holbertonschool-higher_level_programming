#!/usr/bin/python3
"""
This module lists all State objects from the database hbtn_0e_6_usa.
The script uses SQLAlchemy to fetch and display data.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Access command line arguments for connection
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]

        # Create engine to connect to MySQL
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(user, passwd, db_name),
                               pool_pre_ping=True)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session instance
        session = Session()

        # Query all State objects, ordered by id
        states = session.query(State).order_by(State.id).all()

        # Display results in the required format: id: name
        for state in states:
            print("{}: {}".format(state.id, state.name))

        # Close the session
        session.close()
