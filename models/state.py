#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel):
    """ State class 
    Attributes:
        name: input name
        cities: relationship to cities table
    """
    __tablename__ = "states"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state",
            cascade="all, delete, delete-orphan"
        )
    else:
        @property
        def cities(self):
            """ Get a list of cities associeted with this state
            Return:
                return a list of all city instances with a state_id matching the id of the current State
            """
            obj_cities = models.storage.all(models.city.City)
            return [city for city in obj_cities.values()
                    if city.stated_id == self.id]

