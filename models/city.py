#!/usr/bin/python3
"""
City Module for HBNB project
"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from os import getenv
import models


class City(BaseModel, Base):
    """
    This is the class for City
    """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        # state = relationship("State")
        places = relationship('Place', backref='cities') # , cascade='delete'
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """
            initializes city
        """
        super().__init__(*args, **kwargs)
