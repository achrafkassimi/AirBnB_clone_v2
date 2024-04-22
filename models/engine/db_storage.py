#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from models import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
# from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


# Base = declarative_base()

# classes = {"Amenity": Amenity, "City": City, "Place": Place, "Review": Review, "State": State, "User": User}


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
        type = getenv("HBNB_TYPE_STORAGE")
        # print(user, passwd, db, host, env)
        # test = 'mysql+mysqldb://{}:{}@{}/{}'.format( user, passwd, host, db)
        # print(test)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        query4 = []
        if cls:
            # print("123")
            if type(cls) is str:
                cls = eval(cls)
            query4 = self.__session.query(cls)
            print(query4)
            for elem in query4:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            # print("321")
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query4 = self.__session.query(clase)
                for elem in query4:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic
    
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
            self.save()

    def reload(self, remove=False):
        """ reload method """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
