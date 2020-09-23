from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
import os.path
import os
import sys
import csv
import json

def_headers_csv = [
    "id",
    "nome_do_produto",
    "nome_da_empresa",
    "data_de_fabricacao",
    "data_de_validade",
    "numero_de_serie",
    "instrucoes_de_armazenamento"
]


class Inventory:
    @classmethod
    def import_data(cls, dict_value, report_type):
        extension = os.path.splitext(dict_value)[1]

        switcher = {
            '.json': cls.convert_json,
            '.csv': cls.convert_csv,
            '.xml': cls.convert_xml,
        }

        file_parsed = switcher[extension](dict_value)
        print(file_parsed)

        # if report_type == 'simples':
        #     return SimpleReport.generate(file_parsed)
        # elif report_type == 'completo':
        #     return CompleteReport.generate(file_parsed)
        # else:
        #     return "Tipo de relatório inexistente"

    @classmethod
    def convert_csv(cls, file_path):
        dummy_file = 'data/dummy.json'
        with open(file_path, 'r') as file:
            with open(dummy_file, 'w') as json_file:
                csv_info = csv.DictReader(file, delimiter=",")
                json.dump(list(csv_info), json_file)
        file_parsed = cls.convert_json(dummy_file)
        os.remove(dummy_file)
        return file_parsed

    @classmethod
    def convert_json(cls, file_path):
        with open(file_path) as json_file:
            return json.load(json_file)

    @classmethod
    def convert_xml(cls, file_path):
        return(file_path, 'converter XML')
