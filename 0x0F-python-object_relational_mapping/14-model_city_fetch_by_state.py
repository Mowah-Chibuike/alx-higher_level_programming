#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, relationship
    from model_state import Base, State
    from model_city import City

    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        dbname = argv[3]

        engine = create_engine("\
mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, dbname))
        session = Session(bind=engine)
        State.cities = relationship("City", back_populates="states")
        cities = session.query(
                State.name, City).select_from(City).join(
                        State).order_by(City.id).all()
        for state_name, city in cities:
            print("{}: ({}) {}".format(state_name, city.id, city.name))
