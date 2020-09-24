from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
from inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class Inventory(Iterable):
    def externa(self, clazz):
        def interna():
            return clazz.generate(self.products)
        return interna

    def __init__(self, class_importer, arquive):
        self.products = class_importer.import_data(arquive)
        self.report_types = {
            "simple": self.externa(SimpleReport),
            "complete": self.externa(CompleteReport),
        }

    def __iter__(self):
        return InventoryIterator(self.products)

    def generate_report(self, report_type):
        return self.report_types[report_type]()
