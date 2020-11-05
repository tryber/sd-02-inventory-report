from helpers.functions import get_extension
from helpers.interfaces import (IMPORTER, REPORT_TYPE)
from collections.abc import Iterable


class Inventory(Iterable):
    def __init__(self):
        self.data = []

    @classmethod
    def import_data(cls, file_path):
        extension = get_extension(file_path)
        file_data = IMPORTER[extension].import_data(file_path)
        cls.data = file_data

    @classmethod
    def get_report(cls, report_type):
        return REPORT_TYPE[report_type].generate(cls.data)

    @classmethod
    def __iter__(cls, report_type):
        return REPORT_TYPE[report_type].__iter__(cls.data)
