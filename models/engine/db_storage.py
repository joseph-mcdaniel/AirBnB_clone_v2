#!/usr/bin/python3
"""
database storage
"""
from models import base_model, amenity, city, place, review, state, user
from models.base_model import Base
from os import environ, getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    __engine = None
    __session = None

    CNC = {
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')))
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ob_dict = {}
        if cls:
            for ob in self.__session.query(cls):
                ob_key = "{}.{}".format(type(ob).__name__, ob.id)
                ob_dict[ob_key] = ob
        else:
            for clas in DBStorage.CNC.values():
                for ob in self.__session.query(clas):
                    ob_key = "{}.{}".format(type(ob).__name__, ob.id)
                    ob_dict[ob_key] = ob
        return ob_dict

    def new(self, obj):
        if obj:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.remove()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
