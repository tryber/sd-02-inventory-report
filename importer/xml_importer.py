from importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def xml_importer(cls, file):
        root = ET.parse(file).getroot()
        return [
            {child.tag: child.text.strip() for child in record.getchildren()}
            for record in root.findall("record")
        ]

    @classmethod
    def import_data(cls, path_to_file):
        try:
            super().compare_type(".xml", path_to_file)
            with open(path_to_file) as file:
                return cls.xml_importer(file)

        except ValueError:
            print("Extensão inválida")
