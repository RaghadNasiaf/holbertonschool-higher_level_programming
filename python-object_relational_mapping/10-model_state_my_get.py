#!/usr/bin/python3
"""
This module prints the State object id with the name passed as argument.
The script uses SQLAlchemy and is safe from SQL injection.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Ensure 4 arguments are provided: user, pass, db, and state_name
    if len(sys.argv) >= 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]

        # Create engine to connect to the MySQL server
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(user, passwd, db_name),
                               pool_pre_ping=True)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query State object by name using filter
        # SQLAlchemy handles parameterization, protecting against SQL injection
        state = session.query(State).filter(State.name == state_name).first()

        # Display results: id if found, otherwise 'Not found'
        if state:
            print("{}".format(state.id))
        else:
            print("Not found")

        # Close the session properly
        session.close()
