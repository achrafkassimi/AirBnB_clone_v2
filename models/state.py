#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """
    This is the class for State
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            Get a list of City instances with
                state_id equals to the current State.id.

            This is a getter attribute for FileStorage
                relationship between State and City.
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list
