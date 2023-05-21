from __future__ import annotations

from pydantic import BaseModel
"""Representation of all responses from api in object-oriented model. It is using also to validtion"""

class Temparature(BaseModel):
    ID: int | None
    TEMPERATURE: float


class Humidity(BaseModel):
    ID: int | None 
    HUMIDITY: float


class Particles(BaseModel):
    ID: int | None
    PARTICLES: float
