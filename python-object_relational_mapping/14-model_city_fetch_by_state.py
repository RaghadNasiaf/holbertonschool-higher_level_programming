#!/usr/bin/python3
"""
This module lists all City objects from the database hbtn_0e_14_usa.
The results are displayed in the format: <state name>: (<city id>) <city name>.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Ensure 3 arguments are provided
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

        # Query City and State objects using a join
        # Sort by cities.id in ascending order
        query_results = session.query(City, State).join(State).order_by(
            City.id).all()

        # Display results: <state name>: (<city id>) <city name>
        for city, state in query_results:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

        # Close the session properly
        session.close()
