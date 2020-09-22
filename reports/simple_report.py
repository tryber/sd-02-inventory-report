import datetime


class SimpleReport:
    def __init__(self):
        self.__oldest_fabrication = ""
        self.__closest_valid_date = ""
        self.__most_products_employee_name = ""

    def get_dates(products, key):
        return min(products, key=lambda x: x[key])

    
    def generate(products):
        


prod = [
  {
    "id": 1,
    "nome_do_produto": "Uai",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2024-06-02",
    "data_de_validade": "2023-02-20",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 2,
    "nome_do_produto": "Sô",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2021-07-28",
    "data_de_validade": "2023-02-21",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  }
]


SimpleReport.get_dates(prod, "data_de_validade")
SimpleReport.get_dates(prod, "data_de_fabricacao")
