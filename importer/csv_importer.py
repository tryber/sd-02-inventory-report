import csv
from importer.importer import Importer
import os.path


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        extension = os.path.splitext(file_path)[1]
        if not extension == '.csv':
            raise ValueError

        with open(file_path, 'r') as file:
            csv_info = csv.DictReader(file, delimiter=",")
            return list(csv_info)
