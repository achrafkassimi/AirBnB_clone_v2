#!/usr/bin/python3
"""
create a unique FileStorage instance for your application
"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    # print("HBNB_TYPE_STORAGE == db")
    storage = DBStorage()
else:
    # print("FileStorage")
    storage = FileStorage()

storage.reload()