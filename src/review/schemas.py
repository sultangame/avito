from pydantic import BaseModel
from enum import Enum


class ReviewEnum(Enum):
    NONE: str = "NONE"
    BAD: str = "BAD"
    NOT_VERY: str = "NOT_VERY"
    GOOD: str = "GOOD"


class ReviewAdd(BaseModel):
    review: str
