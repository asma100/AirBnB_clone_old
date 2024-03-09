#!/usr/bin/python3
"""Review  Model """

from models.base_model import BaseModel


class Review(BaseModel):
    """Represnts the Review model"""
    place_id = ""
    user_id = ""
    text = ""
