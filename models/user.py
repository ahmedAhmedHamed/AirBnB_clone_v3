#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if self.password is not None:
            md5_hash = hashlib.md5()
            md5_hash.update(self.password.encode('utf8'))
            password = md5_hash.hexdigest()
            self.password = password

    @password.setter
    def password(self, value):
        """setter for password"""
        self.password = self.hash_password(value)

    @staticmethod
    def hash_password(password):
        """hashes password"""
        return hashlib.md5(password.encode('utf-8')).hexdigest()

    def __setattr__(self, key, value):
        """override for when changing password using this function"""
        if key == 'password':
            value = self.hash_password(value)
        super(User, self).__setattr__(key, value)
