#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          backref='state',
                          cascade='all, delete-orphan')
    
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
