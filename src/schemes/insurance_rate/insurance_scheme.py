from datetime import datetime, date

from sqlmodel import SQLModel, Field, Relationship


class InsuranceRateBase(SQLModel):
    id: int | None = Field(primary_key=True)
    cargo_type_id: int = Field(foreign_key='cargo_type.id')
    date: date = Field(nullable=False)
    rate: float = Field(nullable=False)
    created_at: datetime | None = Field(default_factory=datetime.utcnow)


class InsuranceRate(InsuranceRateBase):
    __tablename__ = 'insurance_rate'
    cargo: "CargoType" = Relationship(back_populates='insurance_rate')


from schemes.cargo_type.cargo_type_scheme import CargoType

InsuranceRate.model_rebuild()
