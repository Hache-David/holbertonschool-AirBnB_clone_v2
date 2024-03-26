#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
import os

Base = declarative_base()

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """"""
        MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')
        self.__engine = create_engine(f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}/{MYSQL_DB}", pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""
        self.__session = self.__session() if self.__session else sessionmaker(bind=self.__engine, expire_on_commit=False)()
        dict = {}
        if cls != None:
            for obj in self.__session.query(cls).all():
                key = f'{type(obj).__name__}.{obj.id}'
                dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    key = f'{type(obj).__name__}.{obj.id}'
                    dict[key] = obj
        return dict

    def new(self, obj):
        """"""
        self.__session.add(obj)


    def save(self):
        """"""
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj:
            self.__session.delete(obj)
    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine , expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
