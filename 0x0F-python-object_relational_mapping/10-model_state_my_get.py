#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    a script that lists all State objects from the database hbtn_0e_6_usa
    """

    engine = create_engine("mysql+mysqldb://{}:{}\
            @localhost:3306/{}".format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    newSess = Sess()
    states = newSess.query(State).order_by(State.id).all()
    if len(states) > 0:
        print("{}".format(states.id))
    else:
        print("Not found")
    session.close()
