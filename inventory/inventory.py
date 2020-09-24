import sys
from reports.complete_report import CompleteReport
from reports.simple_report import SimpleReport
from collections.abc import Iterable
from inventory.inventory_iterator import InventoryIterator


class Inventory(Iterable):
    def __init__(self, adapter):
        self._inventory_stock = []
        self.adapter = adapter

    def __iter__(self):
        return InventoryIterator(self._inventory_stock)

    def flag_string(self, flag, report_list):
        flag_obj = {
          'simples': SimpleReport().generate,
          'completo': CompleteReport().complete_report,
        }

        return flag_obj[flag](report_list)

    def get_relatory(self, flag, name_arq):
        report_list = self.adapter().import_data(name_arq)
        self._inventory_stock = report_list
        return self.flag_string(flag, report_list)

    def import_data(self):
        try:
            return self.get_relatory(sys.argv[2].lower(), sys.argv[1])
        except ValueError as ex:
            raise ex