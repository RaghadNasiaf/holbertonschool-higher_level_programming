#!/usr/bin/python3
"""
This module defines the State class that links to the MySQL table states.
It uses SQLAlchemy ORM to map the class to the database table.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the declarative base instance
Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        id (int): The state's unique identifier (primary key).
        name (str): The state's name (max 128 chars, not null).
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
