#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from \
the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, URL
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    if len(argv) > 3:
        user = argv[1]
        passwd = argv[2]
        db = argv[3]

        url = URL.create(
                'mysql+mysqldb',
                host='localhost',
                port=3306,
                username=user,
                password=passwd,
                database=db
        )
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)

        with Session() as session:
            states_a = session.query(State).\
                filter(State.name.contains('a')).all()
            for state in states_a:
                session.delete(state)
            session.commit()
