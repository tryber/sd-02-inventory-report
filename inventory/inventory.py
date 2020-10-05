# import csv
# import json
# import xml.etree.ElementTree as ET
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter
from importer.xml_importer import XmlImporter


class Inventory:
    # @classmethod
    # def csv_converter(cls, file):
    #     products = []
    #     with open(file) as csv_file:
    #         reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
    #         for row in reader:
    #             product = {}
    #             for key, value in dict(row).items():
    #                 if key == "id":
    #                     product[key] = int(value)
    #                 else:
    #                     product[key] = value
    #             products.append(product)
    #     return products

    # @classmethod
    # def json_converter(cls, file):
    #     with open(file) as json_file:
    #         content = json_file.read()
    #         products = json.loads(content)
    #     return products

    # @classmethod
    # def xml_converter(cls, file):
    #     tree = ET.parse(file)
    #     root = tree.getroot()
    #     products = []
    #     for record in root.iter("record"):
    #         product = {}
    #         for child in record.getchildren():
    #             if child.tag == "id":
    #                 product[child.tag] = int(child.text.strip())
    #             else:
    #                 product[child.tag] = child.text.strip()
    #         products.append(product)
    #     return products

    @classmethod
    def import_data(cls, file, report_type):
        if (file.endswith(".csv")):
            # products = cls.csv_converter(file)
            products = CsvImporter.import_data(file)
        if (file.endswith(".json")):
            # products = cls.json_converter(file)
            products = JsonImporter.import_data(file)
        if (file.endswith(".xml")):
            # products = cls.xml_converter(file)
            products = XmlImporter.import_data(file)

        if report_type == "simples":
            return SimpleReport.generate(products)
        if report_type == "completo":
            return CompleteReport.generate(products)
