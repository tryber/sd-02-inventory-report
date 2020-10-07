from importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path_to_file):
        try:
            super().compare_type(".json", path_to_file)
            with open(path_to_file) as file:
                return json.load(file)

        except ValueError:
            print("Extensão inválida")
