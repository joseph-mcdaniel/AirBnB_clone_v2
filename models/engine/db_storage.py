#!/usr/bin/python3
"""
database storage
"""
from models import base_model, amenity, city, place, review, state, user
from models.base_model import Base
from os import environ, getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')))
        """
        self.__models = {'User': User,
                         'Amenity': Amenity,
                         'City': City,
                         'Place': Place,
                         'Review': Review,
                         'State': State}
        """
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj = {}
        if cls:
            for object in self.__session.query(self.__models[cls]):
                obj[object.__dict__['id']] = object
        return obj

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
