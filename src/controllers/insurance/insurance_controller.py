from fastapi import APIRouter, Depends
from sqlmodel import Session

from db import get_session
from models.insurance import insurance_model
from models.user.auth_model import get_current_user
from schemes.constant.request_body import RatesByDate, InsuranceCostRequest
from schemes.insurance.insurance_scheme import InsuranceCost
from schemes.user.user_scheme import User

insurance_router = APIRouter(
    prefix="/insurance",
    tags=["Insurance"]
)


@insurance_router.post("/upload/", response_model='',
                       description="Func for getting info about client by his id")
async def upload_insurance_rates(
    body: list[RatesByDate],
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    insurance_model.upload_insurance(session, body)


@insurance_router.post("/cost/", response_model=InsuranceCost,
                       description="Func for getting insurance cost by cargo type & date")
async def get_insurance_cost(
    body: InsuranceCostRequest,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    return insurance_model.get_insurance_cost(session, body)
