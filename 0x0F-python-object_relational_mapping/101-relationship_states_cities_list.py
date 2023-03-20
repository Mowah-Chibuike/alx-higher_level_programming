#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects, contained in the
database hbtn_0e_101_usa using the SQLAlchemy module
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, relationship
    from relationship_state import Base, State
    from relationship_city import City

    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        dbname = argv[3]

        engine = create_engine("\
mysql+mysqldb://{}:{}@localhost/{}".format(username, password, dbname))
        session = Session(bind=engine)
        cities = session.query(City).order_by(City.state_id).all()
        states = {}
        for city in cities:
            if states.__contains__(city.state.name):
                states[city.state.name].append(city)
            else:
                states[city.state.name] = [city]
        for state, cities in states.items():
            print("{}: {}".format(cities[0].state_id, state))
            for city in cities:
                print("\t{}: {}".format(city.id, city.name))

