import requests as r
import json as j

EXCHANGE_RATE_KEY = 'mid'

response = r.get(r'http://api.nbp.pl/api/exchangerates/rates/A/USD/2023-03-07/')

response_as_json = j.loads(response.text)

print('Kurs PLN/USD na dzień '+response_as_json['rates'][0]['effectiveDate']+' wynosi '+str(response_as_json['rates'][0][EXCHANGE_RATE_KEY]))
