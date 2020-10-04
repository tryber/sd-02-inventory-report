import math
from datetime import datetime, date
from operator import itemgetter
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, dict_file):
        production = (sorted(dict_file, key=lambda i: i['data_de_fabricacao']))
        expiration_date = None
        days_diff = math.inf

        most_products = Counter(
            industry["nome_da_empresa"] for industry in dict_file
        ).most_common(1)[0][0]

        for index, industry in enumerate(dict_file):
            today = datetime.now().strftime("%Y-%m-%d")
            if industry["data_de_validade"] > today:
                expiration_date_test = industry['data_de_validade']

        nearest_shelf_life = min(
            [
                prod
                for prod in dict_file
                if prod["data_de_validade"]
                >= datetime.now().strftime("%Y-%m-%d")
            ],
            key=itemgetter("data_de_validade"),
        )["data_de_validade"]

        for index, industry in enumerate(dict_file):
            today = datetime.strptime(str(date.today()), '%Y-%m-%d')
            converted_exp = datetime.strptime(
                industry['data_de_validade'], '%Y-%m-%d')
            date_diff = abs((today - converted_exp).days)

            if (date_diff < days_diff):
                days_diff = date_diff
                expiration_date = industry['data_de_validade']

        return(
            f'Data de fabricação mais antiga:'
            f' {production[0]["data_de_fabricacao"]}\n'
            f'Data de validade mais próxima: {expiration_date}\n'
            f'16-21: {expiration_date_test}\n'
            f'22-30: {nearest_shelf_life}\n'
            f'Empresa com maior quantidade de produtos estocados:'
            f' {most_products}')
