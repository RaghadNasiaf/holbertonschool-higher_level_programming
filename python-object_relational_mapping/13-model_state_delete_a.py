#!/usr/bin/python3
"""
This module deletes all State objects containing the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create engine and session to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete states containing the letter 'a'
    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        session.delete(state)

    # Commit changes and close the session
    session.commit()
    session.close()
