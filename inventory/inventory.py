from helpers.functions import get_extension
from helpers.interfaces import (
    IMPORTER, REPORT_TYPE)
# from helpers.constants import (ERROR_EXTENSION, ERROR_NOT_FOUND)
from collections.abc import Iterable
# from helpers.classes import Check
# import csv
# import json
# import xmltodict
from inventory.inventory_iterator import InventoryIterator


class Inventory(Iterable):
    def __init__(self):
        self.data = []

    def import_data(self, file_path):
        extension = get_extension(file_path)
        file_data = IMPORTER[extension].import_data(file_path)
        self.data = file_data
        # if (extension == "csv"):
        #     cls.data = cls.import_data_csv(file_path)
        # elif (extension == "json"):
        #     cls.data = cls.import_data_json(file_path)
        # elif (extension == "xml"):
        #     cls.data = cls.import_data_xml(file_path)

    def get_report(self, report_type):
        return REPORT_TYPE[report_type].generate(self.data)

    # o for chama este __iter__
    def __iter__(self):
        return InventoryIterator(self.data)

    # @classmethod
    # def import_data_csv(cls, file_path):
    #     extension = get_extension(file_path)
    #     Check.check_element(extension, "csv", ERROR_EXTENSION)
    #     try:
    #         with open(file_path) as csv_file:
    #             csv_reader = csv.DictReader(csv_file, delimiter=",")
    #             data = []
    #             for csv_row in csv_reader:
    #                 data.append(csv_row)
    #     except(FileNotFoundError):
    #         raise ValueError(ERROR_NOT_FOUND)
    #     else:
    #         return data

    # @classmethod
    # def import_data_json(cls, file_path):
    #     extension = get_extension(file_path)
    #     Check.check_element(extension, "json", ERROR_EXTENSION)
    #     try:
    #         with open(file_path) as json_file:
    #             data = json.load(json_file)
    #     except(FileNotFoundError):
    #         raise ValueError(ERROR_NOT_FOUND)
    #     else:
    #         return data

    # @classmethod
    # def import_data_xml(cls, file_path):
    #     extension = get_extension(file_path)
    #     Check.check_element(extension, "xml", ERROR_EXTENSION)
    #     try:
    #         with open(file_path) as xml_file:
    #             xml_reader = xmltodict.parse(xml_file.read())[
    #                 "dataset"]["record"]
    #             data = []
    #             for xml_row in xml_reader:
    #                 data.append(xml_row)
    #     except(FileNotFoundError):
    #         raise ValueError(ERROR_NOT_FOUND)
    #     else:
    #         return data
