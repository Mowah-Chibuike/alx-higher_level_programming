#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco” from the
database hbtn_0e_100_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_city import City
    from relationship_state import Base, State

    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        dbname = argv[3]

        engine = create_engine("\
mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, dbname))
        Base.metadata.create_all(engine)
        session = Session(bind=engine)
        new_state = State(name="California")
        session.add(new_state)
        session.commit()
        new_state.cities = [City(name="San Francisco")]
        session.commit()
