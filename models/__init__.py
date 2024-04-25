#!/usr/bin/python3
"""
create a unique FileStorage instance for your application
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    # print("HBNB_TYPE_STORAGE == db")
    storage = DBStorage()
    storage.reload()
else:
    # print("FileStorage")
    storage = FileStorage()
    storage.reload()
