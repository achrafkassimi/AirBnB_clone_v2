#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            temp = {}
            for key in FileStorage.__objects.keys():
                if cls.__name__ in key:
                    temp[key] = FileStorage.__objects[key]
            return temp
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """delete obj from __objects"""
        if (obj is None):
            return
        if (obj):
            del(obj)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """ close method """
        self.reload()
# """
# This module defines a class to manage file storage for hbnb clone
# """
# import json
# from models.base_model import BaseModel
# from models.user import User
# from models.place import Place
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.review import Review
# import shlex

# classes = {
#             "Amenity": Amenity,
#             "BaseModel": BaseModel,
#             "City": City,
#             "Place": Place,
#             "Review": Review,
#             "State": State,
#             "User": User}


# class FileStorage:
#     """
#     This class manages storage of hbnb models in JSON format
#     """
#     __file_path = 'file.json'
#     __objects = {}

#     def all(self, cls=None):
#         """
#         Returns a dictionary of models currently in storage.
#         Args:
#             cls (class, optional):
#                 If specified, filters the result to include
#                 only objects of the specified class.
#         Returns:
#             dict: A dictionary containing objects in storage.
#         """
#         if cls is not None:
#             new_dict = {}
#             for key, value in self.__objects.items():
#                 if cls == value.__class__ or cls == value.__class__.__name__:
#                     new_dict[key] = value
#             return new_dict
#         return self.__objects

#     def new(self, obj):
#         """Adds new object to storage dictionary"""
#         if obj is not None:
#             key = obj.__class__.__name__ + "." + obj.id
#             self.__objects[key] = obj

#     def save(self):
#         """Saves storage dictionary to file"""
#         json_objects = {}
#         for key in self.__objects:
#             json_objects[key] = self.__objects[key].to_dict()
#         with open(self.__file_path, 'w') as f:
#             json.dump(json_objects, f)

#     def reload(self):
#         """Loads storage dictionary from file"""
#         try:
#             with open(self.__file_path, 'r') as f:
#                 jo = json.load(f)
#             for key in jo:
#                 self.__objects[key] = classes[jo[key]["__class__"]]
# (**jo[key])
#         except FileNotFoundError:
#             pass

#     def delete(self, obj=None):
#         """
#         Delete obj from __objects if it s inside
#             - if obj is equal to None,
#         the method should not do anything
#         """
#         if obj is not None:
#             key = obj.__class__.__name__ + '.' + obj.id
#             if key in self.__objects:
#                 del self.__objects[key]

#     def close(self):
#         """
#         call reload() method for deserializing the JSON file to objects
#         """
#         self.reload()
