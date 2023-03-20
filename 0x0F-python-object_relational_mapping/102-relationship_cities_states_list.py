#!/usr/bin/python3
"""
lists all City objects, and corresponding States, contained in the
database hbtn_0e_101_usa using the SQLAlchemy module
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City

    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        dbname = argv[3]

        engine = create_engine("\
mysql+mysqldb://{}:{}@localhost/{}".format(username, password, dbname))
        session = Session(bind=engine)
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))
