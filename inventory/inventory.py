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
