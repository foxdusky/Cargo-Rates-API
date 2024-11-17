from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship


class CargoTypeBase(SQLModel):
    id: int | None = Field(primary_key=True)
    name: str = Field(nullable=False, unique=True)
    created_at: datetime | None = Field(default_factory=datetime.utcnow)


class CargoType(CargoTypeBase, table=True):
    __tablename__ = 'cargo_type'
    rates: list["InsuranceRate"] = Relationship(back_populates='cargo')
