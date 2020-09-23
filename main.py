from inventory.inventory import Inventory
from importer.xml_importer import XmlImporter
from importer.json_importer import JsonImporter
from importer.csv_importer import CsvImporter
import sys
import os.path

# print(Inventory.import_data('simple', 'data/inventory_20200823.xml'))

# print(Inventory.convert_xml_to_Dict('data/inventory_20200823.xml'))

# XmlImporter.import_data('data/inventory_20200823.xml')

strategy = {
    ".json": JsonImporter,
    ".csv": CsvImporter,
    ".xml": XmlImporter
}

type_report = sys.argv[2]
path_to_file = sys.argv[1]
extension = os.path.splitext(path_to_file)[1]

print(
    Inventory.import_data(
        type_report, strategy[extension], path_to_file
    )
)
