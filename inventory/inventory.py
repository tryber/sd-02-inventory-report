from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
from inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class Inventory(Iterable):
    def __init__(self, conversor):
        self.file_parsed = []
        self.conversor = conversor
    
    def __iter__(self):
        return InventoryIterator(self.file_parsed)

    def import_data(self, dict_value, report_type):
        self.file_parsed = self.conversor.import_data(dict_value)

        if report_type == 'simples':
            return SimpleReport.generate(self.file_parsed)
        elif report_type == 'completo':
            return CompleteReport.generate(self.file_parsed)
        else:
            return "Tipo de relatório inexistente"
