#!/usr/bin/python3
"""
a script that lists all cities objects from the database hbtn_0e_6_usa
"""


from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    a script that lists all cities objects from the database hbtn_0e_6_usa
    """

    engine = create_engine("mysql+mysqldb://{}:{}\
            @localhost:3306/{}".format(argv[1], argv[2], argv[3]))
    Sess = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    newSess = Sess()
    cities = newSess.query(City).order_by(CIty.id.asc()).all()
    for names in cities:
        print("{}: ({}) {}".format(names.state.name, names.id, names.name))
    newSess.close()
