from datetime import datetime, date

from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal


class InsuranceRateBase(SQLModel):
    id: int | None = Field(primary_key=True)
    cargo_type_id: int = Field(foreign_key='cargo_type.id')
    insurance_date: date = Field(nullable=False)
    percent: float = Field(nullable=False)
    created_at: datetime | None = Field(default_factory=datetime.utcnow)


class InsuranceRate(InsuranceRateBase, table=True):
    __tablename__ = 'insurance_rate'
    cargo: "CargoType" = Relationship(back_populates='rates')


class InsuranceCost(InsuranceRateBase):
    insurance_price: Decimal | None = None
