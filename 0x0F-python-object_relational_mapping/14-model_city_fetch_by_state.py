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
    from model_city import City

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
            results = session.query(State, City).\
                filter(State.id == City.state_id).\
                order_by(City.id).all()
            for row in results:
                state = row[0]
                city = row[1]
                print(f"{state.name}: ({city.id}) {city.name}")
