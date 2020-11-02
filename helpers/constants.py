AVAILABLE_EXTENSIONS = ("csv", "json", "xml")

AVAILABLE_TYPES = ("completo", "simples")

ERROR_ARGUMENTS = "Missing some arguments"

ERROR_EXTENSION = "Invalid extension"

ERROR_NOT_FOUND = "File not found"

ERROR_TYPE = "Report type doesn't available"

EXPECTED_DATA = [{"id": "1", "nome_do_produto": "Melodrama", "nome_da_empresa": "Lorde", "data_de_fabricacao": "2017-05-16", "data_de_validade": "2022-09-17", "numero_de_serie": "CR25 1551 4467 2549 4402 6CSG D20", "instrucoes_de_armazenamento": "Broadcast the boom boom boom boom And make 'em all dance to it"}, {"id": "2", "nome_do_produto": "Ultraviolence", "nome_da_empresa": "Lana Del Rey", "data_de_fabricacao": "2014-05-13", "data_de_validade": "2022-12-25", "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20", "instrucoes_de_armazenamento": "He hit me and it felt like a kiss"}, {"id": "3", "nome_do_produto": "Norman Fucking Rockwell!",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "nome_da_empresa": "Lana Del Rey", "data_de_fabricacao": "2019-08-30", "data_de_validade": "2030-10-11", "numero_de_serie": "CZ09 8588 0858 8435 9140 2695", "instrucoes_de_armazenamento": "If he's a serial killer then what's the worst That could happen to a girl who's already hurt?"}, {"id": "4", "nome_do_produto": "folklore", "nome_da_empresa": "Taylor Swift", "data_de_fabricacao": "2020-06-24", "data_de_validade": "2022-12-25", "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN", "instrucoes_de_armazenamento": "They told me all of my cages were mental So I got wasted like all my potential"}]
EXPECTED_COMPLETE_REPORT = """
Data de fabricação mais antiga: 2014-05-13
Data de validade mais próxima: 2022-09-17
Empresa com maior quantidade de produtos estocados: Lana Del Rey

Produtos estocados por empresa:
- Lana Del Rey: 2
- Lorde: 1
- Taylor Swift: 1
"""

EXPECTED_SIMPLE_REPORT = """
Data de fabricação mais antiga: 2014-05-13
Data de validade mais próxima: 2022-09-17
Empresa com maior quantidade de produtos estocados: Lana Del Rey
"""

PATH_INVALID_EXTENSION = "/home/anderson.bolivar/Documents/projects/sd-02-inventory-report/data/inventory.txt"

PATH_NOT_EXIST_CSV = "/home/anderson.bolivar/Documents/projects/sd-02-inventory-report/data/not_exists.csv"

PATH_NOT_EXIST_JSON = "/home/anderson.bolivar/Documents/projects/sd-02-inventory-report/data/not_exists.json"

PATH_NOT_EXIST_XML = "/home/anderson.bolivar/Documents/projects/sd-02-inventory-report/data/not_exists.xml"

PATH_VALID_CSV = "/home/anderson.bolivar/Documents/projects/sd-02-inventory-report/data/test_inventory.csv"

PATH_VALID_JSON = "/home/anderson.bolivar/Documents/projects/sd-02-inventory-report/data/test_inventory.json"

PATH_VALID_XML = "/home/anderson.bolivar/Documents/projects/sd-02-inventory-report/data/test_inventory.xml"
