from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
from inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class Inventory(Iterable):

    def __init__(self, class_importer, arquive):
        self.products = class_importer.import_data(arquive)

    def __iter__(self):
        return InventoryIterator(self.products)

    def generate_report(self, report_type):

        if report_type == "simple":
            return SimpleReport.generate(self.products)
        if report_type == "complete":
            return CompleteReport.generate(self.products)
