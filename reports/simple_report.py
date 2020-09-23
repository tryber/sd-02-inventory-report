from datetime import datetime
from operator import itemgetter
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, products):
        oldest_fabrication = min(
            products, key=itemgetter("data_de_fabricacao")
        )["data_de_fabricacao"]
        nearest_shelf_life = min(
            [
                prod
                for prod in products
                if prod["data_de_validade"]
                >= datetime.now().strftime("%Y-%m-%d")
            ],
            key=itemgetter("data_de_validade"),
        )["data_de_validade"]
        most_products_company_name = max(
            Counter(prod["nome_da_empresa"] for prod in products)
        )
        result = ''
        result += f"Data de fabricação mais antiga: {oldest_fabrication}\n"
        result += f"Data de validade mais próxima: {nearest_shelf_life}\n"
        result += f"Empresa com maior quantidade de produtos estocados: {most_products_company_name}\n"
        return result

if __name__ == "__main__":
    products = [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2024-06-02",
            "data_de_validade": "2023-01-01",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus",
        },
        {
            "id": 2,
            "nome_do_produto": "Sô",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2021-07-28",
            "data_de_validade": "2021-01-10",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus",
        },
        {
            "id": 3,
            "nome_do_produto": "Uai Sô",
            "nome_da_empresa": "Folgado Inc.",
            "data_de_fabricacao": "2021-07-22",
            "data_de_validade": "2021-01-11",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus",
        },
    ]
  

    print(SimpleReport.generate(products))
