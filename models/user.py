#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models import storage_type


class User(BaseModel):
    """This class defines a user by various attributes
    Attributes:
        email: the email field
        password: the password
        first_name: input for first_name
        last_name: input for last_name
    """
    __tablename__ = "users"
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
