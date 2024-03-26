#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
    
    if HBNB_TYPE_STORAGE == 'db':
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            all_cities = storage.all(City)
            state_cities = [city for city in all_cities.values() if city.state_id == self.id]
            return state_cities
