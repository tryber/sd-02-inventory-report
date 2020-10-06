import math
from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, dict_file):
        production = (sorted(dict_file, key=lambda i: i['data_de_fabricacao']))
        expiration_date = None
        days_diff = -math.inf

        most_products = Counter(
            industry["nome_da_empresa"] for industry in dict_file
        ).most_common(1)[0][0]

        for index, industry in enumerate(dict_file):
            today = datetime.now()
            converted_exp = datetime.strptime(
                industry['data_de_validade'], '%Y-%m-%d')
            date_diff = (today - converted_exp).days

            if (date_diff > days_diff and date_diff <= 0):
                days_diff = date_diff
                expiration_date = industry['data_de_validade']

        return(
            f'Data de fabricação mais antiga:'
            f' {production[0]["data_de_fabricacao"]}\n'
            f'Data de validade mais próxima: {expiration_date}\n'
            f'Empresa com maior quantidade de produtos estocados:'
            f' {most_products}')
