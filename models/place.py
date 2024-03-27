#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer,default=0, nullable=False)
    max_guest = Column(Integer,default=0, nullable=False)
    price_by_night = Column(Integer,default=0, nullable=False)
    latitude = Column(float, nullable=True)
    longitude = Column(float, nullable=True)
    amenity_ids = []
