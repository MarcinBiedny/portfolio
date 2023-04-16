import requests as r
import json as j

EXCHANGE_RATE_KEY = 'mid'
HTTP_STATUS_OK = 200

response = r.get(r'http://api.nbp.pl/api/exchangerates/rates/A/USD/2023-04-09/')
print(response.status_code)
if response.status_code == HTTP_STATUS_OK:
    response_as_json = j.loads(response.text)
    print('Kurs PLN/USD na dzień '+response_as_json['rates'][0]['effectiveDate']+' wynosi '+str(response_as_json['rates'][0][EXCHANGE_RATE_KEY]))

else:
    print("Something was wrong. Unexpected response status code: " + str(response.status_code))
