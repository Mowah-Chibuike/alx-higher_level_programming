#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, URL, text
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sqlalchemy.exc import NoResultFound 

    if len(argv) > 4:
        user = argv[1]
        password = argv[2]
        database = argv[3]
        search_name = argv[4]

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
        try:
            state = session.query(State).filter(State.name == search_name).one()
            print(f"{state.id}")
        except NoResultFound:
            print('Nothing')
