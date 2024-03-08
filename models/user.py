#!/usr/bin/python3
"""Defines the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represnts the user.
    Attributes:
        email: user email.
        password: user's password.
        first_name: user's first name.
        last_name: user's last name.
        """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
