#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, URL, text
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) > 3:
        user = argv[1]
        password = argv[2]
        database = argv[3]

        url = URL.create(
                "mysql+mysqldb",
                username=user,
                password=password,
                host='localhost',
                port=3306,
                database=database
        )
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        session = Session(bind=engine)
        states = session.query(State).filter(State.name.contains('a'))\
            .order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")
