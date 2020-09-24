from inventory.inventory import Inventory
from importer.json_importer import JsonImporter
from importer.csv_importer import CsvImporter
from importer.xml_importer import XmlImporter
import sys

try:
    inventory = Inventory(XmlImporter)

    print(inventory.import_data('data/inventory_20200823.xml', 'simples'))

except KeyError:
    print("Tipo de arquivo inválido", file=sys.stderr)
    sys.exit(1)

except ValueError:
    print("Formato de arquivo inválido", file=sys.stderr)
    sys.exit(1)
