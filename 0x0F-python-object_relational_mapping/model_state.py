#!/usr/bin/python3
"""
a python file that contains the class definition of a
state and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    a python file that contains the class definition of a
    state and an instance Base = declarative_base()
    """

    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
