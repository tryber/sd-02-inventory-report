import json
import math
from datetime import datetime, timedelta, date
from collections import Counter

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
expiration_date = None
days_diff = math.inf
most_products = Counter(empresa["nome_da_empresa"] for empresa in data).most_common(1)[0][0]
print(most_products)
# percorrer todos os 
for index, industry in enumerate(data):
    today = datetime.strptime(str(date.today()), '%Y-%m-%d')
    converted_exp = datetime.strptime(industry['data_de_validade'], '%Y-%m-%d')
    date_diff = abs((today - converted_exp).days)
    if (date_diff < days_diff):
        days_diff = date_diff
        expiration_date = industry['data_de_validade']

print(f'Data de fabricação mais antiga: {production[0]["data_de_fabricacao"]}')
print(f'Data de validade mais próxima: {expiration_date}')
print(f'Empresa com maior quantidade de produtos estocados: {most_products}')

