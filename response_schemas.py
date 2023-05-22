from __future__ import annotations

from pydantic import BaseModel, Extra
"""Representation of all responses from api in object-oriented model. It is using also to validtion"""

class PreconfiguredBaseModel(BaseModel):
    """Base class with config for all responses models"""
    class Config:
        extra = Extra.forbid


class Temparature(PreconfiguredBaseModel):
    ID: int | None
    TEMPERATURE: float


class Humidity(PreconfiguredBaseModel):
    ID: int | None 
    HUMIDITY: float


class Particles(PreconfiguredBaseModel):
    ID: int | None
    PARTICLES: float
