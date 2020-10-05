import csv
import json
import xml.etree.ElementTree as ET
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def csv_converter(cls, file):
        products = []
        with open(file) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
            for row in reader:
                products.append(dict(row))
        return products

    @classmethod
    def json_converter(cls, file):
        with open(file) as json_file:
            content = json_file.read()
            products = json.loads(content)
        return products

    @classmethod
    def xml_converter(cls, file):
        tree = ET.parse(file)
        root = tree.getroot()
        products = []
        for record in root.iter("record"):
            product = {}
            for child in record.getchildren():
                product[child.tag] = child.text.strip()
            products.append(product)
        return products

    @classmethod
    def import_data(cls, file, report_type):
        if (file.endswith(".csv")):
            products = cls.csv_converter(file)
        if (file.endswith(".json")):
            products = cls.json_converter(file)
        if (file.endswith(".xml")):
            products = cls.xml_converter(file)

        if report_type == "simples":
            return SimpleReport.generate(products)
        if report_type == "completo":
            return CompleteReport.generate(products)
