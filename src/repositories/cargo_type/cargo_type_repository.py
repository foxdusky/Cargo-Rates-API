from sqlmodel import Session, select

from schemes.cargo_type.cargo_type_scheme import CargoType


def get_cargo_type_by_id(session: Session, cargo_type_id: int) -> CargoType | None:
    st = select(CargoType).where(CargoType.id == cargo_type_id)
    return session.exec(st).first()


def create_cargo_type(session: Session, cargo_type: CargoType) -> CargoType:
    session.add(cargo_type)
    session.commit()
    session.refresh(cargo_type)
    return cargo_type


def update_cargo_type(session: Session, cargo_type: CargoType) -> CargoType:
    db_cargo_type = session.merge(cargo_type)
    session.commit()
    session.refresh(db_cargo_type)
    return db_cargo_type


def delete_cargo_type(session: Session, cargo_type: CargoType) -> CargoType:
    session.delete(cargo_type)
    session.commit()
    return cargo_type
