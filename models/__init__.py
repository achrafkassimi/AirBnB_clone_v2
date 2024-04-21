#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# from dotenv import load_dotenv
# load_dotenv() echo 'all State' |
# HBNB_MYSQL_USER=hbnb_dev
# HBNB_MYSQL_PWD=hbnb_dev_pwd
# HBNB_MYSQL_HOST=localhost
# HBNB_MYSQL_DB=hbnb_dev_db
# HBNB_TYPE_STORAGE=db
# ./console.py
# print(getenv("HBNB_TYPE_STORAGE"))

if getenv("HBNB_TYPE_STORAGE") == "db":
    print("HBNB_TYPE_STORAGE == db")
    storage = DBStorage()
    storage.reload()
else:
    print("FileStorage")
    storage = FileStorage()
    storage.reload()
