#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, URL
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    if len(argv) > 3:
        username = argv[1]
        password = argv[2]
        database = argv[3]

        url = URL.create(
                'mysql+mysqldb',
                host='localhost',
                port=3306,
                username=username,
                password=password,
                database=database
        )

        engine = create_engine(url)
        Base.metadata.create_all(engine)
        Session = sessionmaker(engine)

        with Session() as session:
            new_state = State(name='Louisiana')
            session.add(new_state)
            session.commit()
            print(new_state.id)
