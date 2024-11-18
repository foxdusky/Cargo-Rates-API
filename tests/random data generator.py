import json
import random
from datetime import datetime, timedelta, date

from pydantic import BaseModel

from schemes.constant.request_body import RatesByDate, _CargoRate
import requests as req

server_connect_link = "http://localhost:8080"
name = 'sample'
passwd = '123'

materials = [
    "Steel", "Aluminum", "Copper", "Wood", "Glass", "Plastic", "Rubber", "Silicon",
    "Carbon Fiber", "Leather", "Wool", "Cotton", "Silk", "Polyester", "Nylon", "Acrylic",
    "Concrete", "Brick", "Ceramic", "Porcelain", "Granite", "Marble", "Sandstone",
    "Asphalt", "Bamboo", "Hemp", "Linen", "Velvet", "Denim", "Canvas", "Cardboard",
    "Paper", "Foam", "Polycarbonate", "Titanium", "Bronze", "Brass", "Gold", "Silver",
    "Platinum", "Nickel", "Zinc", "Lead", "Tin", "Fiberglass", "Graphite", "Ivory",
    "Slate", "Charcoal", "Plexiglass"
]


class Request(BaseModel):
    body: list[RatesByDate]


def generate_random_date(start_date: str, end_date: str) -> date:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_date = start + timedelta(days=random_days)
    return random_date.date()


def generate_random_rate() -> float:
    return random.uniform(0.001, 0.08)


def get_random_material(prev_choice: list | None = None) -> str:
    return random.choice(materials)


def generate_random_request_data() -> Request:
    st_date = "2024-01-01"
    e_date = "2024-12-31"
    num_of_dates = 10  # Quantity of dates
    num_of_exemplars = 10  # Quantity of exemplars of materials for every one date
    list_of_exemplars: list[RatesByDate] = []
    for i in range(num_of_dates):
        rand_date = generate_random_date(st_date, e_date)
        rates: list[_CargoRate] = []
        for j in range(num_of_exemplars):
            rates.append(
                _CargoRate(
                    cargo_name=get_random_material(),
                    rate=generate_random_rate()
                )
            )
        list_of_exemplars.append(
            RatesByDate(
                ins_date=rand_date,
                rates=rates
            )
        )
    return Request(body=list_of_exemplars)


def reg():
    response = req.post(
        f'{server_connect_link}/user/create/',

        params={
            'username': name,
            'password': passwd
        }
    )

    return response.json()


def api_request(data: Request) -> None:
    api_key = reg()
    json_data = [
        {
            "ins_date": item.ins_date.isoformat(),
            "rates": [{"cargo_name": rate.cargo_name, "rate": rate.rate} for rate in item.rates]
        }
        for item in data.body
    ]

    response = req.post(
        f'{server_connect_link}/insurance/upload',
        headers={'Authorization': f"Bearer {api_key['access_token']}"},
        json=json_data  # Преобразуем в JSON формат
    )
    if response.status_code == 200:
        print("Request successful:", response.json())
    else:
        print(f"Request failed. Status code: {response.status_code}, Response: {response.text}")


if __name__ == "__main__":
    _data = generate_random_request_data()
    api_request(_data)
