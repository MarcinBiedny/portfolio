countries_and_capitals = {'Poland': 'Warsaw',
                          'Czechia': 'Prague',
                          'Germany': 'Berlin'}

try:
    print(countries_and_capitals['USA'])
except KeyError:
    print("Klucz nie został znaleziony")