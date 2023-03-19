#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database
hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) >= 5:
        username = argv[1]
        password = argv[2]
        dbname = argv[3]
        state_name = argv[4]

        engine = create_engine("\
mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, dbname))
        session = Session(bind=engine)
        state = session.query(State).filter(text("name=:name")).params(name=state_name).first()
        if state is not None:
            print(state.id)
        else:
            print("Not found")
