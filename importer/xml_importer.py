from importer.importer import Importer
from xml.dom import minidom


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path_to_file):
        try:
            super().compare_type(".xml", path_to_file)
            xml = minidom.parse(path_to_file)
            records = xml.getElementsByTagName("record")
            return [
                {
                    node.tagName: node.firstChild.data
                    for node in record.childNodes
                }
                for record in records
            ]

        except ValueError:
            print("Extensão inválida")
