#!/usr/bin/python3
"""
contains the class definition of a State and an instance Base = \
declarative_base()
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (Column, Integer, String)

Base = declarative_base()


class State(Base):
    """
links to the MySQL table state and is used by the ORM to map rows to \
instances of State
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan',
                          order_by='City.id')
