# import csv
# import json
# import xml.etree.ElementTree as ET
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
from collections.abc import Iterable
from inventory.inventory_iterator import InventoryIterator


class Inventory(Iterable):
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

    # @classmethod
    # def import_data(cls, file, report_type):
    #     if (file.endswith(".csv")):
    #         products = cls.csv_converter(file)
    #     if (file.endswith(".json")):
    #         products = cls.json_converter(file)
    #     if (file.endswith(".xml")):
    #         products = cls.xml_converter(file)

    #     if report_type == "simples":
    #         return SimpleReport.generate(products)
    #     if report_type == "completo":
    #         return CompleteReport.generate(products)

    def __init__(self, importer):
        self.importer = importer
        self.products = []

    def __iter__(self):
        return InventoryIterator(self.products)

    def import_data(self, file, report_type):
        self.products = self.importer.import_data(file)

        if report_type == "simples":
            return SimpleReport.generate(self.products)
        if report_type == "completo":
            return CompleteReport.generate(self.products)
