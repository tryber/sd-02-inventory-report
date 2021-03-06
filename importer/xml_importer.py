from helpers.classes import Check
from helpers.constants import (ERROR_EXTENSION, ERROR_NOT_FOUND)
from helpers.functions import get_extension
from importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        extension = get_extension(file_path)
        Check.check_element(extension, "xml", ERROR_EXTENSION)
        try:
            with open(file_path) as xml_file:
                xml_reader = xmltodict.parse(xml_file.read())[
                    "dataset"]["record"]
                data = []
                for xml_row in xml_reader:
                    data.append(xml_row)
        except(FileNotFoundError):
            raise ValueError(ERROR_NOT_FOUND)
        else:
            return data
