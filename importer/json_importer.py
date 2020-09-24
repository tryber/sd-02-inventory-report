from importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(self, arq_name):
        with open(f"data/{arq_name}") as file:
            content = file.read()
            return json.loads(content)
