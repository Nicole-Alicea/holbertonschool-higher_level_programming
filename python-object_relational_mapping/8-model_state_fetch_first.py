#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    _state = session.query(State).order_by(State.id).first()

    if _state:
        print("{}: {}".format(_state.id, _state.name))
    else:
        print("Nothing")
    session.close()