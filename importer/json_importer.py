from helpers.classes import Check
from helpers.constants import (ERROR_EXTENSION, ERROR_NOT_FOUND)
from helpers.functions import get_extension
from importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        extension = get_extension(file_path)
        Check.check_element(extension, "json", ERROR_EXTENSION)
        try:
            with open(file_path) as json_file:
                data = json.load(json_file)
        except(FileNotFoundError):
            raise ValueError(ERROR_NOT_FOUND)
        else:
            return data
