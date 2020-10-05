from importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if not file.endswith(".json"):
            raise ValueError("Extensão de arquivo inválida")
        with open(file) as json_file:
            content = json_file.read()
            products = json.loads(content)
        return products
