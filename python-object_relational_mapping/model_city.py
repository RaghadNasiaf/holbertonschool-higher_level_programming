#!/usr/bin/python3
"""
This module defines the City class that links to the MySQL table cities.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class that inherits from Base and links to the MySQL table cities.

    Attributes:
        id (int): Auto-generated, unique integer, primary key.
        name (str): String with maximum 128 characters, can't be null.
        state_id (int): Foreign key to states.id, can't be null.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
