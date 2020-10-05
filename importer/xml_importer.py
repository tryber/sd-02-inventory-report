from importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if not file.endswith(".xml"):
            raise ValueError("Extensão de arquivo inválida")
        tree = ET.parse(file)
        root = tree.getroot()
        products = []
        for record in root.iter("record"):
            product = {}
            for child in record.getchildren():
                if child.tag == "id":
                    product[child.tag] = int(child.text.strip())
                else:
                    product[child.tag] = child.text.strip()
            products.append(product)
        return products
