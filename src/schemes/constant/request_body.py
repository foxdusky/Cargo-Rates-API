from datetime import date
from typing import Literal

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


class _CargoRate(SQLModel):
    cargo_name: str = Field(
        description="Type of cargo",
        nullable=False,
    )
    rate: float = Field(
        description="Insurance rate in float percent",
        nullable=False,
    )


class RatesByDate(SQLModel):
    ins_date: date = Field(
        description="Date of insurance rates",
        nullable=False,
    )
    rates: list[_CargoRate]


class InsuranceCostRequest(SQLModel):
    declared_value: float
    cargo_type: str
    ins_date: date | None = None
