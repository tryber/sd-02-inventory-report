import xml.etree.ElementTree as ET
from importer.importer import Importer
import os.path


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        extension = os.path.splitext(file_path)[1]
        if not extension == '.xml':
            raise ValueError

        tree = ET.parse(file_path)
        root = tree.getroot()
        lista = []

        for elem in root.iter('record'):
            obj = {}
            for child in elem:
                obj[child.tag] = child.text
            lista.append(obj)

        return lista
