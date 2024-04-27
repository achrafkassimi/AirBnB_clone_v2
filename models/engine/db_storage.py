#!/usr/bin/python3
"""
new class for DBStorage
"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"State": State, "City": City, "User": User
        , "Place": Place,"Review": Review, "Amenity": Amenity}


class DBStorage:
    """
    interaacts with the MySQL database
    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}?charset=latin1'
            .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                    HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
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
        # new_dict = {}
        # for clss in classes:
        #     if cls is None or cls is classes[clss] or cls is clss:
        #         objs = self.__session.query(classes[clss]).all()
        #         for obj in objs:
        #             key = obj.__class__.__name__ + '.' + obj.id
        #             new_dict[key] = obj
        # return (new_dict)

    def new(self, obj):
        """
        add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """
        save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete an element in the table
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload method """
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        print(ses)
        Session = scoped_session(ses)
        print(Session)
        self.__session = Session

    def close(self):
        """ close method """
        # self.__session.close()
        self.__session.remove()
