import json
import math
from datetime import datetime, date
from collections import Counter

class SimpleReport:
    def generate(self, dict_file):
        production = (sorted(data, key = lambda i: i['data_de_fabricacao']))
        # expiration = (sorted(data, key = lambda i: i['data_de_validade']))
        expiration_date = None
        days_diff = math.inf
        most_products = Counter(empresa["nome_da_empresa"] for empresa in data).most_common(1)[0][0]
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

# daqui pra baixo tem q ser removido, se quiser deixar automatizado

with open('../data/inventory_20200823.json') as json_file:
    data = json.load(json_file)

new_report = SimpleReport()
new_report.generate(data)
