from typing import List
from pydantic import BaseModel
# import os
import requests

url = 'http://api.nbp.pl/api/exchangerates/rates/B/EUR/'
response = requests.get(url)
print(response)
data = response.json()
print(data)
print("---------------------------------")
print(data['rates'][0]['mid'])

class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class CurrencyInfo(BaseModel):
    table: str
    code: str
    rates: List[Rate]

currency_info = CurrencyInfo(**data)
print(currency_info)
print("Kurs eur:", currency_info.rates[0].mid)
# os.system('cls')


