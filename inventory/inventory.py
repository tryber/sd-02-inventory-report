import csv
from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory():
    @classmethod
    def report_type(cls, file, type):
        if type == 'simples':
            return SimpleReport.generate(file)
        if type == 'completo':
            return CompleteReport.generate(file)

    @classmethod
    def csv_importer(cls, file, type):
        all_products = []
        with open(file) as products:
            csv_products = csv.DictReader(
                products, delimiter=",", quotechar='"'
            )
            for row in csv_products:
                all_products.append(dict(row))
        return cls.report_type(all_products, type)

    @classmethod
    def import_data(cls, file, type):
        if file.endswith(".csv"):
            return cls.csv_importer(file, type)
