from datetime import date
from typing import Literal, Dict, List

from pydantic.v1 import BaseModel
from sqlmodel import SQLModel, Field


class GetALLRequestBody(SQLModel):
    limit: int | None = Field(
        description="Limit of returning exemplars",
        nullable=True,
        default=None
    )
    offset: int | None = Field(
        description="Offset of returning exemplars",
        nullable=True,
        default=None
    )
    sort_field: str | None = Field(
        description="Field name for sorting, like an name of parameters in search filter",
        nullable=True,
        default=None
    )
    sort_direction: Literal['asc', 'desc'] | None = None
    # In child class filter names as search_filter: ClassOfTheMainObject


class _CargoRate(BaseModel):
    cargo_type: str
    rate: str


class InsuranceRateUpload(BaseModel):
    __root__: Dict[date, List[_CargoRate]]
