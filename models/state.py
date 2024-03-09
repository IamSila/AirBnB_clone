#!/usr/bin/python3
"""
Defines a class called state that inherits from basemodel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represent a state

    Attributes:
        name (str): The name of the state

    """
    name = ""
