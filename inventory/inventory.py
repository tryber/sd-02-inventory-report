from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
from inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class Inventory(Iterable):
    def __init__(self, clazz, arquive):
        self.products = clazz.import_data(arquive)
        self.report_types = {
            "simple": self.importer_generate(SimpleReport),
            "complete": self.importer_generate(CompleteReport),
        }

    def importer_generate(self, clazz):
        def interna():
            return clazz.generate(self.products)
        return interna

    def __iter__(self):
        return InventoryIterator(self.products)

    def generate_report(self, report_type):
        return self.report_types[report_type]()


# import csv
# import json
# import os.path
# from reports.simple_report import SimpleReport
# import xml.etree.ElementTree as ET

# class Inventory():
#     def import_date(self, path_to_file, report_type):
#         try:
#             extension = os.path.splitext(path_to_file)[1]
#             if '.csv' != extension:
#                 raise ValueError
#             with open(path_to_file) as file:
#                 header, *csvLines = csv.reader(file, delimiter=",")
#                 arr = [
#                     {item: line[index] for index, item in enumerate(header)}
#                     for line in csvLines
#                 ]
#                 report_types = {
#                     "simple": SimpleReport.generate(arr),
#                     "complete": CompleteReport.generate(arr),
#                 }
#                 return report_types[report_type]

#         except ValueError:
#             print("Extensão inválida")

# class Inventory():
#     def import_date(self, path_to_file, report_type):
#         try:
#             extension = os.path.splitext(path_to_file)[1]
#             if '.json' != extension:
#                 raise ValueError
#             with open(path_to_file) as file:
#                 arr = json.load(file)
#                 report_types = {
#                     "simple": SimpleReport.generate(arr),
#                     "complete": CompleteReport.generate(arr),
#                 }
#                 return report_types[report_type]

#         except ValueError:
#             print("Extensão inválida")

# class Inventory():
#     def import_date(self, path_to_file, report_type):
#         try:
#             extension = os.path.splitext(path_to_file)[1]
#             if '.xml' != extension:
#                 raise ValueError
#             with open(path_to_file) as file:
#                 root = ET.parse(file).getroot()
#                 arr = self.arquivo(root)
#                 report_types = {
#                     "simple": SimpleReport.generate(arr),
#                     "complete": CompleteReport.generate(arr),
#                 }
#                 return report_types[report_type]

#         except ValueError:
#             print("Extensão inválida")

#     def arquivo(cls, root):
#         return [
#                     {child.tag: child.text.strip()
#                         for child in record.getchildren()}
#                     for record in root.findall("record")
#                 ]
