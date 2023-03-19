#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the database
hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) == 4:
        username = argv[1]
        password = argv[2]
        dbname = argv[3]

        engine = create_engine("\
mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, dbname))
        session = Session(bind=engine)
        states = session.query(State).filter(
                State.name.like("%a%")).order_by(State.id).all()
        for state in states:
            print("{}: {}".format(state.id, state.name))
