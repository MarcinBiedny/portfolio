import requests as r
import json as j
import datetime
from typing import Union

EXCHANGE_RATE_KEY = 'mid'
HTTP_STATUS_OK = 200
USER_INPUT_RETRY_END_COUNT = 2

table_currency_code_mapping = {
    "A": ["USD", "AUD", "EUR", "CHF"],
    "B": ["ZMW", "MDL", "ARS"],
}

def getCurrencyCodeTable(currency_code) -> Union[str, None]:
    for table in table_currency_code_mapping.keys():
        if currency_code in table_currency_code_mapping[table]:
            return table

    return None

print("This program allows you to check the average rates of the following currencies: USD, AUD, EUR, CHF, JPN, ZMW (kwacha zambijska), MDL (lej Mołdawii), ARS (peso argentyńskie).")

for user_input_count in range(1, USER_INPUT_RETRY_END_COUNT + 1):
    currency_code = input(
        "Please enter the currency you want to check:\n").upper()

    table = getCurrencyCodeTable(currency_code)
    if table == None:
        print("Unfortunately, I do not know such currency.")
    else:
        break

    if user_input_count == USER_INPUT_RETRY_END_COUNT and table == None:
        print("Zaduża liczba prób.. żegnam ozięble!")
        quit()

table = getCurrencyCodeTable(currency_code)

date_as_string = input("Please enter the date in the format YYYY-MM-DD:\n")

url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{currency_code}/{date_as_string}/"
response = r.get(url)

date = datetime.datetime.strptime(date_as_string, '%Y-%m-%d').date()
while response.status_code != HTTP_STATUS_OK:
    date_as_string = date.strftime('%Y-%m-%d')
    url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{currency_code}/{date_as_string}/"
    response = r.get(url)
    date = date - datetime.timedelta(days=1)

response_as_json = j.loads(response.text)

print("Kurs PLN/{} tabela {} na dzień {} wynosi {}".format(
    currency_code,
    table,
    response_as_json['rates'][0]['effectiveDate'],
    str(response_as_json['rates'][0][EXCHANGE_RATE_KEY])
))
