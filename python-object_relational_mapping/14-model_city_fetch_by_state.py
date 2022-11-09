#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_city = session.query(State.name, City.id, City.name) \
                        .filter(State.id == City.state_id).order_by(City.id)

    for c in state_city:
        print("{:s}: ({:d}) {:s}".format(c[0], c[1], c[2]))