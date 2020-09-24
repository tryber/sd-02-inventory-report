import sys
import re
from reports.complete_report import CompleteReport
from reports.simple_report import SimpleReport
from importer.xml_importer import XmlImporter
from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter
from collections.abc import Iterable
from inventory.inventory_iterator import InventoryIterator


class Inventory(Iterable):
    def __init__(self):
        self._inventory_stock = []

    def __iter__(self):
        return InventoryIterator(self._inventory_stock)

    def flag_string(self, flag, report_list):
        flag_obj = {
          'simples': SimpleReport().generate,
          'completo': CompleteReport().complete_report,
        }

        return flag_obj[flag](report_list)

    def csv(self, flag, name_arq):
        report_list = CsvImporter().import_data(name_arq)
        self._inventory_stock = report_list
        return self.flag_string(flag, report_list)

    def json(self, flag, name_arq):
        report_list = JsonImporter().import_data(name_arq)
        self._inventory_stock = report_list
        return self.flag_string(flag, report_list)

    def xml(self, flag, name_arq):
        report_list = XmlImporter().import_data(name_arq)
        self._inventory_stock = report_list
        return self.flag_string(flag, report_list)

    def import_data(self):
        extension = sys.argv[1].split(".")[1].lower()
        flag = sys.argv[2].lower()
        ext_obj = {
            "csv": self.csv,
            "json": self.json,
            "xml": self.xml,
        }
        try:
            if re.search(".(csv|json|xml)$", f".{extension}", re.IGNORECASE):
                return ext_obj[extension](flag, sys.argv[1])
            else:
                return "extensao incorreta"
        except Exception as ex:
            return ex
