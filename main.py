from inventory.inventory import Inventory
import sys
from importer.xml_importer import XmlImporter
from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter

extension = sys.argv[1].split(".")[1].lower()
try:
    ext_obj = {
        "csv": CsvImporter,
        "json": JsonImporter,
        "xml": XmlImporter,
    }
    inventory = Inventory(ext_obj[extension])
    print(inventory.import_data())
    iterator = iter(inventory)
    first_item = next(iterator)
    print(first_item)
except Exception:
    print('Formato Inválido', file=sys.stderr)
