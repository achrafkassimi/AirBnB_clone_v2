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

classes = {
            "Amenity": Amenity,
            # "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User}


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
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

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
        Query on the curret database session all objects of the given class.
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
            # self.save()

    def reload(self): #, remove=False
        """ reload method """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        # if remove:
        #     Session.remove()
        self.__session = Session()

    def close(self):
        """ close method """
        self.__session.close()
        # self.reload(remove=True)

    # def reload(self):
    #     """
    #     reload method
    #     """
    #     Base.metadata.create_all(self.__engine)
    #     sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
    #     Session = scoped_session(sec)
    #     self.__session = Session
    #
    # def close(self):
    #     """
    #     calls remove()
    #     """
    #     self.__session.remove()
    #
    # def all(self, cls=None):
    # """
    # returns a dictionary
    # Return:
    #     returns a dictionary of __object
    # """
    # new_dict = {}
    # for clss in classes:
    #     if cls is None or cls is classes[clss] or cls is clss:
    #         objs = self.__session.query(classes[clss]).all()
    #         for obj in objs:
    #             key = obj.__class__.__name__ + '.' + obj.id
    #             new_dict[key] = obj
    # return (new_dict)
