from pydantic import BaseModel

from station.rest.types import LinesColors
from station.rest.validators import NotEmptyLinesAndColorsValidatorMixin


class Property(BaseModel, NotEmptyLinesAndColorsValidatorMixin):
    disabled: bool
    name: str
    fa: str
    colors: list[LinesColors]
    lines: list[int]


class Relation(BaseModel, NotEmptyLinesAndColorsValidatorMixin):
    disabled: bool
    name: str
    fa: str
    colors: list[LinesColors]
    lines: list[int]


class Station(BaseModel):
    property: Property
    relations: list[Relation]
