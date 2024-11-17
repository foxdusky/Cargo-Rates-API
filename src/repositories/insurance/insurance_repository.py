from sqlalchemy.orm import joinedload
from sqlmodel import Session, select

from schemes.insurance.insurance_scheme import InsuranceRate
from datetime import date


def get_insurance_rate_by_id(session: Session, insurance_id: int) -> InsuranceRate | None:
    st = select(InsuranceRate).where(InsuranceRate.id == insurance_id)
    return session.exec(st).first()


def get_insurance_by_cargo_id_and_date(session: Session, cargo_id: int, insurance_date: date) -> InsuranceRate | None:
    st = select(InsuranceRate)
    st = st.where(InsuranceRate.insurance_date == insurance_date)
    st = st.where(InsuranceRate.cargo_type_id == cargo_id)
    st = st.options(joinedload(InsuranceRate.cargo))
    return session.exec(st).first()


def create_insurance_rate(session: Session, insurance_rate: InsuranceRate) -> InsuranceRate:
    session.add(insurance_rate)
    session.commit()
    session.refresh(insurance_rate)
    return insurance_rate


def update_insurance_rate(session: Session, insurance_rate: InsuranceRate) -> InsuranceRate:
    db_insurance_rate = session.merge(insurance_rate)
    session.commit()
    session.refresh(db_insurance_rate)
    return db_insurance_rate


def delete_insurance_rate(session: Session, insurance_rate: InsuranceRate) -> InsuranceRate:
    session.delete(insurance_rate)
    session.commit()
    return insurance_rate
