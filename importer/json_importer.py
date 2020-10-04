from importer.importer import Importer
import json
import re


class JsonImporter(Importer):
    def import_data(self, arq_name):
        if re.search(".json$", arq_name, re.IGNORECASE):
            print(arq_name)
            with open(f"{arq_name}") as file:
                content = file.read()
                return json.loads(content)
        else:
            raise "Formato Inválido"
