#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from models import *
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


Base = declarative_base()

# classes = {"Amenity": Amenity, "City": City,
#            "Place": Place, "Review": Review, "State": State, "User": User}


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
        test = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db)
        print(test)

        self.__engine = create_engine(test, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.

        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

        # """returns a dictionary
        # Return:
        #     returns a dictionary of __object
        # """
        # dic = {}
        # if cls:
        #     if type(cls) is str:
        #         cls = eval(cls)
        #     query = self.__session.query(cls)
        #     for elem in query:
        #         key = "{}.{}".format(type(elem).__name__,
        #                              elem.id)
        #         dic[key] = elem
        # else:
        #     lista = [State, City, User,
        #              Place, Review, Amenity]
        #     for clase in lista:
        #         query = self.__session.query(clase)
        #         for elem in query:
        #             key = "{}.{}".format(type(elem).__name__,
        #                                  elem.id)
        #             dic[key] = elem
        # return (dic)

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
        print(self.__engine)
        metadata = MetaData(bind=self.__engine)
        print(metadata)
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
