#!/usr/bin/python3
"""This is the review class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from os import getenv
import models
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """
    This is the class for Review
    """
    if models.storage_t == 'db':
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
        # user = relationship(
            # 'User', back_populates='reviews')  # cascade? slave
        # place = relationship(
        #     'Place', back_populates='reviews')  # cascade? slave
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
