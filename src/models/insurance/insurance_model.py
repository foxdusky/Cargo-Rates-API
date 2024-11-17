from datetime import datetime

from fastapi import HTTPException, status
from sqlmodel import Session

from repositories.cargo import cargo_type_repository
from repositories.insurance import insurance_repository
from schemes.cargo.cargo_type_scheme import CargoType
from schemes.constant.request_body import RatesByDate, InsuranceCostRequest
from schemes.insurance.insurance_scheme import InsuranceRate, InsuranceCost

#######################################################
#                                                     #
#               Made by Dusky Fox                     #
#                                                     #
#######################################################

def upload_insurance(session: Session, data: list[RatesByDate]) -> None:
    for date in data:
        for cargo in date.rates:
            # check for existence of cargo type in db
            cargo.cargo_name = cargo.cargo_name.lower()
            cargo_obj = cargo_type_repository.get_cargo_by_uniquename(session, cargo.cargo_name)
            if not cargo_obj:
                _cargo_obj = CargoType(
                    name=cargo.cargo_name,
                )
                cargo_obj = cargo_type_repository.create_cargo_type(session, _cargo_obj)

            insurance_record = insurance_repository.get_insurance_by_cargo_id_and_date(
                session,
                cargo_id=cargo_obj.id,
                insurance_date=date.ins_date
            )
            # Creating insurance record
            if not insurance_record:
                insurance_record: InsuranceRate = InsuranceRate(
                    cargo_type_id=cargo_obj.id,
                    insurance_date=date.ins_date,
                    percent=cargo.rate
                )
                insurance_repository.create_insurance_rate(session, insurance_record)


def get_insurance_cost(session: Session, body: InsuranceCostRequest) -> InsuranceCost:
    if not body.ins_date:
        body.ins_date = datetime.utcnow()
    body.cargo_type = body.cargo_type.lower()
    _cargo = cargo_type_repository.get_cargo_by_uniquename(session, body.cargo_type)
    if not _cargo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Here's no any records of cargo type: {body.cargo_type}",
        )
    insurance_record = insurance_repository.get_insurance_by_cargo_id_and_date(
        session,
        cargo_id=_cargo.id,
        insurance_date=body.ins_date
    )
    if not insurance_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Here's no any records of insurance rate for cargo type: {body.cargo_type} and for date: {body.ins_date}",
        )

    data = InsuranceCost(**insurance_record.model_dump())
    data.insurance_price = body.declared_value * insurance_record.percent
    return data
