from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
import os.path
import os
import csv
import json
import xml.etree.ElementTree as ET


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
        # print(file_parsed)
        if report_type == 'simples':
            return SimpleReport.generate(file_parsed)
        elif report_type == 'completo':
            return CompleteReport.generate(file_parsed)
        else:
            return "Tipo de relatório inexistente"

    @classmethod
    def convert_csv(cls, file_path):
        with open(file_path, 'r') as file:
            csv_info = csv.DictReader(file, delimiter=",")
            return list(csv_info)

    @classmethod
    def convert_json(cls, file_path):
        with open(file_path) as json_file:
            return json.load(json_file)

    @classmethod
    def convert_xml(cls, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        lista = []

        for elem in root.iter('record'):
            obj = {}
            for child in elem:
                obj[child.tag] = child.text
            lista.append(obj)

        return lista
