import requests as r
import json as j

EXCHANGE_RATE_KEY = 'mid'
HTTP_STATUS_OK = 200

currencies_and_tables = {"USD": "A",
                         "AUD": "A",
                         "EUR": "A",
                         "CHF": "A",
                         "JPN": "A",
                         "ZMW": "B",
                         "MDL": "B",
                         "ARS": "B",}

print("This program allows you to check the average rates of the following currencies:: USD, AUD, EUR, CHF, JPN, ZMW (kwacha zambijska), MDL (lej Mołdawii), ARS (peso argentyńskie), ")

currency = input("Please enter the currency you want to check: \n")
#table = currencies_and_tables[currency.upper()]

while currency.upper() not in currencies_and_tables:
    print("Unfortunately, I do not know such currency.")
    currency = input("Please enter the currency you want to check: \n")

table = currencies_and_tables[currency.upper()]

#print(currencies_and_tables.get(currency))

date = input("Please enter the date in the format YYYY-MM-DD: ")
url = f"http://api.nbp.pl/api/exchangerates/rates/{table}/{currency}/{date}/"
response = r.get(url)

#response = r.get(r'http://api.nbp.pl/api/exchangerates/rates/A/USD/2023-04-19/')
print(response.status_code)
if response.status_code == HTTP_STATUS_OK:
    response_as_json = j.loads(response.text)
    print('Kurs PLN/'+currency.upper()+' na dzień '+response_as_json['rates'][0]['effectiveDate']+' wynosi '+str(response_as_json['rates'][0][EXCHANGE_RATE_KEY]))

else:
    print("Something was wrong. Unexpected response status code: " + str(response.status_code))