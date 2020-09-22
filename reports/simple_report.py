import json
from datetime import datetime, timedelta, date

with open('../data/inventory_20200823.json') as json_file:
    data = json.load(json_file)

class SimpleReport:
    def generate(self, dict_file):
        for index, industry in enumerate(data):
            print(index, industry['data_de_fabricacao'])
            # print("Data de fabricação mais antiga: YYYY-MM-DD")
            # print("Data de validade mais próxima: YYYY-MM-DD")
            # print("Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA")

production = (sorted(data, key = lambda i: i['data_de_fabricacao']))
expiration = (sorted(data, key = lambda i: i['data_de_validade']))
today = date.today()
print("Today's date:", today)

for index, industry in enumerate(data):
    today = datetime.strptime(str(date.today()), '%Y-%m-%d')
    converted_exp = datetime.strptime(industry['data_de_validade'], '%Y-%m-%d')
    date_diff = abs((today - converted_exp).days)
    print(date_diff)
    
    # print("Data de fabricação mais antiga: YYYY-MM-DD")
    # print("Data de validade mais próxima: YYYY-MM-DD")
    # print("Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA")

