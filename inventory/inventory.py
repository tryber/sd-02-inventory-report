import csv
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
    def import_data(cls, file, report_type):
        if (file.endswith(".csv")):
            products = cls.csv_converter(file)
        print(products)
        if report_type == "simples":
            return SimpleReport.generate(products)
        if report_type == "completo":
            return CompleteReport.generate(products)
