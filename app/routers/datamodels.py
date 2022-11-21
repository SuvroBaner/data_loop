"""
    This module defines the Datamodel for the API input request
"""

__version__ = '0.1'
__author__ = 'suvrobaner@gmail.com'

from pydantic import BaseModel
from datetime import datetime

class InputRequest(BaseModel):
    text: str