from inventory.inventory import Inventory
from importer.xml_importer import XmlImporter
from importer.json_importer import JsonImporter
from importer.csv_importer import CsvImporter
import sys
import os.path


# strategy = {
#     ".json": JsonImporter,
#     ".csv": CsvImporter,
#     ".xml": XmlImporter
# }

# report_type = sys.argv[1]
# path_to_file = sys.argv[2]
# extension = os.path.splitext(path_to_file)[1]


# inventory = Inventory(strategy[extension], path_to_file)
# products_report = inventory.generate_report(report_type)
# print(products_report)

# iterator = iter(inventory)
# first_item = next(iterator)
# print(first_item)
