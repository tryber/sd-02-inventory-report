import json
from importer.importer import Importer
import os.path


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        extension = os.path.splitext(file_path)[1]
        if not extension == '.json':
            raise ValueError

        with open(file_path) as json_file:
            return json.load(json_file)
