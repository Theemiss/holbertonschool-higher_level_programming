#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(
                                        sys.argv[1],
                                        sys.argv[2],
                                        sys.argv[3]
                                            ),
                            pool_pre_ping=True
                                )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    re = session.query(State).all()
    for x in re:
        print("{}: {}".format(x.id, x.name))
        for r in x.cities:
            print("    {}: {}".format(r.id, r.name))
    session.close()
