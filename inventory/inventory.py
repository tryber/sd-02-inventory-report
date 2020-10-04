import sys
from reports.complete_report import CompleteReport
from reports.simple_report import SimpleReport
from collections.abc import Iterable
from inventory.inventory_iterator import InventoryIterator
# from importer.csv_importer import CsvImporter
# from importer.json_importer import JsonImporter
# from importer.xml_importer import XmlImporter


class Inventory(Iterable):
    def __init__(self, adapter):
        self._inventory_stock = []
        self.adapter = adapter

    def __iter__(self):
        return InventoryIterator(self._inventory_stock)

    def flag_string(self, flag, report_list):
        flag_obj = {
          'simples': SimpleReport().generate,
          'completo': CompleteReport().generate_complete,
        }

        return flag_obj[flag](report_list)

    def get_relatory(self, flag, name_arq):
        report_list = self.adapter().import_data(name_arq)
        self._inventory_stock = report_list
        return self.flag_string(flag, report_list)

    # def csv(self, flag, name_arq):
    #     report_list = CsvImporter().import_data(name_arq)
    #     self._inventory_stock = report_list
    #     return self.flag_string(flag, report_list)

    # def json(self, flag, name_arq):
    #     report_list = JsonImporter().import_data(name_arq)
    #     self._inventory_stock = report_list
    #     return self.flag_string(flag, report_list)

    # def xml(self, flag, name_arq):
    #     report_list = XmlImporter().import_data(name_arq)
    #     self._inventory_stock = report_list
    #     return self.flag_string(flag, report_list)

    def import_data(self):
        # extension = sys.argv[1].split(".")[1].lower()
        # flag = sys.argv[2].lower()
        # ext_obj = {
        #     "csv": self.csv,
        #     "json": self.json,
        #     "xml": self.xml,
        # }
        try:
            # return ext_obj[extension](flag, sys.argv[1])
            return self.get_relatory(sys.argv[2].lower(), sys.argv[1])
        except ValueError as ex:
            raise ex
