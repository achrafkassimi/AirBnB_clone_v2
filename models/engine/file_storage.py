#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex


class FileStorage:
    """
    This class manages storage of hbnb models in JSON format
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.
        Args:
            cls (class, optional): 
                If specified, filters the result to include
                only objects of the specified class.
        Returns:
            dict: A dictionary containing objects in storage.
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects
        # if cls:
        #     if isinstance(cls, str):
        #         cls = globals().get(cls)
        #     if cls and issubclass(cls, BaseModel):
        #         cls_dict = {k: v for k,
        #                     v in self.__objects.items() 
        #                     if isinstance(v, cls)}
        #         return cls_dict
        # return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # self.all().update( {obj.to_dict()['__class__'] + '.' + obj.id: obj} )
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)
        # with open(self.__file_path, 'w') as f:
        #     temp = {}
        #     temp.update(self.__objects)
        #     for key, val in temp.items():
        #         temp[key] = val.to_dict()
        #     json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
        # classes = {
        #             'BaseModel': BaseModel,
        #             'User': User, 'Place': Place,
        #             'State': State, 'City': City, 
        #             'Amenity': Amenity, 'Review': Review
        #           }
        # try:
        #     temp = {}
        #     with open(self.__file_path, 'r') as f:
        #         temp = json.load(f)
        #         for key, val in temp.items():
        #                 val = eval(val["__class__"])(**val)
        #                 self.__objects[key] = val
        # except FileNotFoundError:
        #     pass
        # except json.decoder.JSONDecodeError:
        #     pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if it's inside 
            - if obj is equal to None,
        the method should not do anything
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]
        # if obj is None:
        #     return
        # obj_to_del = f"{obj.__class__.__name__}.{obj.id}"

        # try:
        #     del self.__objects[obj_to_del]
        # except AttributeError:
        #     pass
        # except KeyboardInterrupt:
        #     pass

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()