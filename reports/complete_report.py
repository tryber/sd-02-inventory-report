from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        return super().generate(products)


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

print(CompleteReport.generate(products))
