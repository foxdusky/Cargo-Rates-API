from sqlmodel import Session, select

from schemes.insurance.insurance_scheme import InsuranceRate


def get_insurance_rate_by_id(session: Session, insurance_id: int) -> InsuranceRate | None:
    st = select(InsuranceRate).where(InsuranceRate.id == insurance_id)
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
