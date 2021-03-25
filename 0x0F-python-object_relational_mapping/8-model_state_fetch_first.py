#!/usr/bin/python3
"""
script that lists all State objects
from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


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
    session = Session(engine)
    re = session.query(State).order_by(State.id).first()
    if re is None:
        print("Nothing")
    else:
        print("{}: {}".format(re.id, re.name))
    session.close()
