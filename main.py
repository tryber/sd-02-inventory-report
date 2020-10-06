from inventory.inventory import Inventory
from importer.json_importer import JsonImporter
from importer.csv_importer import CsvImporter
from importer.xml_importer import XmlImporter
import sys
import os

try:
    extension = os.path.splitext(sys.argv[1])[1]
    switcher = {
        '.json': JsonImporter,
        '.csv': CsvImporter,
        '.xml': XmlImporter,
    }

    inventory = Inventory(switcher[extension])
    print(inventory.import_data(sys.argv[1], sys.argv[2]))

except KeyError:
    print("Tipo de arquivo inválido", file=sys.stderr)
    sys.exit(1)

except ValueError:
    print("Formato de arquivo inválido", file=sys.stderr)
    sys.exit(1)

except IndexError:
    print("Favor inserir arquivo e tipo do relatório", file=sys.stderr)
    sys.exit(1)
