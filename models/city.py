#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel):
    """ The city class
    Attributes:
        name: input name
        state_id: the state id
    """
    __tablename__ = "cities"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    else:
        name = ""
        state_id = ""
