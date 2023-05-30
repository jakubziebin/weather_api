from __future__ import annotations

from pydantic import BaseModel, Extra

from datetime import date
"""Representation of all responses from api in object-oriented model. It is using also to validtion"""

class PreconfiguredBaseModel(BaseModel):
    """Base class with config for all responses models"""
    class Config:
        extra = Extra.forbid


class Temparature(PreconfiguredBaseModel):
    ID: int | None
    TEMPERATURE: float
    DATE: date | None

class Humidity(PreconfiguredBaseModel):
    ID: int | None 
    HUMIDITY: float
    DATE: date | None


class Particles(PreconfiguredBaseModel):
    ID: int | None
    PARTICLES: float
    DATE: date | None
