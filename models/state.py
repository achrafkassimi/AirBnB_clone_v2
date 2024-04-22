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
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade='all, delete, delete-orphan', backref="state")
    else:
        @property
        def cities(self):
            """Get a list of City instances with
                state_id equals to the current State.id.

            This is a getter attribute for FileStorage
                relationship between State and City.
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)

            return city_list



# class State(BaseModel, Base):
    # """ State class """
    # __tablename__ = "states"

    # if getenv("HBNB_TYPE_STORAGE") == "db":
    #     name = Column(String(128), nullable=False)
    #     cities = relationship("City", backref="state", cascade="all, delete")
    # else:
    #     name =""

    #     @property
    #     def cities(self):
    #         """Get a list of City instances with
    #             state_id equals to the current State.id.

    #         This is a getter attribute for FileStorage
    #             relationship between State and City.
    #         """
    #         city_list = []
    #         for city in models.storage.all(City).values():
    #             if getattr(city, "state_id") == self.id:
    #                 city_list.append(city)
    #         return (city_list)

    # cities = relationship('City',
    #                       backref='state',
    #                       cascade='all, delete-orphan')
    
    # def __init__(self, *args, **kwargs):
    #     """initializes state"""
    #     super().__init__(*args, **kwargs)

    # @property
    # def cities(self):
    #     var = models.storage.all()
    #     lista = []
    #     result = []
    #     for key in var:
    #         city = key.replace('.', ' ')
    #         city = shlex.split(city)
    #         if (city[0] == 'City'):
    #             lista.append(var[key])
    #     for elem in lista:
    #         if (elem.state_id == self.id):
    #             result.append(elem)
    #     return (result)
