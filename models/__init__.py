#!/usr/bin/python3
"""
create a unique FileStorage instance for your application
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    # print("HBNB_TYPE_STORAGE == db")
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    # print("FileStorage")
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
