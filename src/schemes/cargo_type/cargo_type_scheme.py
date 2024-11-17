from datetime import datetime

from sqlmodel import SQLModel, Field, Relationship


class CargoTypeBase(SQLModel):
    id: int | None = Field(primary_key=True)
    name: str = Field(nullable=False, unique=True)
    created_at: datetime | None = Field(default_factory=datetime.utcnow)


class CargoType(CargoTypeBase):
    __tablename__ = 'cargo_type'
    insurance_rate: list["InsuranceRate"] = Relationship(back_populates='cargo')


from schemes.insurance_rate.insurance_scheme import InsuranceRate

CargoType.model_rebuild()
