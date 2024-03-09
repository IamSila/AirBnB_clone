#!/usr/bin/python3
"""
Defines the User class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

        Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string



    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
