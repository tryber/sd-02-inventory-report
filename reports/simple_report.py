
from helpers.functions import (get_elements, get_nearest_date)


class SimpleReport:
    @classmethod
    def generate(cls, data):
        fabrication_dates = get_elements(data, "data_de_fabricacao")
        expiration_dates = get_elements(data, "data_de_validade")
        companies = get_elements(data, "nome_da_empresa")
        oldest_fabrication_date = min(fabrication_dates)
        newest_expiration_date = get_nearest_date(expiration_dates)
        higher_products_company = max(set(companies), key=companies.count)
        return """
Data de fabricação mais antiga: {}
Data de validade mais próxima: {}
Empresa com maior quantidade de produtos estocados: {}
""".format(oldest_fabrication_date, newest_expiration_date,  higher_products_company)
