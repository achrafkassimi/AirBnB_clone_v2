#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        # print(user, passwd, db, host, env)
        test = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db)
        # print(test)

        self.__engine = create_engine(test,
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine,
                           expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session

    def close(self):
        """ calls remove()
        """
        self.__session.remove()
