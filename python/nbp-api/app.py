import requests as r
import json as j
import datetime

EXCHANGE_RATE_KEY = 'mid'
HTTP_STATUS_OK = 200

currencies_and_tables = {
    "USD": "A",
    "AUD": "A",
    "EUR": "A",
    "CHF": "A",
    "JPN": "A",
    "ZMW": "B",
    "MDL": "B",
    "ARS": "B",
}

print("This program allows you to check the average rates of the following currencies: USD, AUD, EUR, CHF, JPN, ZMW (kwacha zambijska), MDL (lej Mołdawii), ARS (peso argentyńskie).")

currency = input("Please enter the currency you want to check:\n")

while currency.upper() not in currencies_and_tables:
    print("Unfortunately, I do not know such currency.")
    currency = input("Please enter the currency you want to check:\n")

table = currencies_and_tables[currency.upper()]

date = input("Please enter the date in the format YYYY-MM-DD:\n")

url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/{date}/"
response = r.get(url)

#print(response.status_code)

while response.status_code != HTTP_STATUS_OK:
    new_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    new_date = new_date - datetime.timedelta(days=1)
    date = new_date.strftime('%Y-%m-%d')
    url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/{date}/"
    response = r.get(url)

response_as_json = j.loads(response.text)
print('The PLN/'+currency.upper()+' exchange rate as of '+response_as_json['rates'][0]['effectiveDate']+' is '+str(response_as_json['rates'][0][EXCHANGE_RATE_KEY]))
