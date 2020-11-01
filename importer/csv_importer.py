from helpers.classes import Check
from helpers.constants import (ERROR_EXTENSION, ERROR_NOT_FOUND)
from helpers.functions import get_extension
from importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        extension = get_extension(file_path)
        Check.check_element(extension, "csv", ERROR_EXTENSION)
        try:
            with open(file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=",")
                data = []
                for csv_row in csv_reader:
                    data.append(csv_row)
        except(FileNotFoundError):
            raise ValueError(ERROR_NOT_FOUND)
        else:
            return data
