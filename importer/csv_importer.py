from importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path_to_file):
        try:
            print(path_to_file)
            super().compare_type(".csv", path_to_file)
            with open(path_to_file) as file:
                header, *csvLines = csv.reader(file, delimiter=",")
                return [
                    {item: line[index] for index, item in enumerate(header)}
                    for line in csvLines
                ]
        except ValueError:
            print("Extensão inválida")
