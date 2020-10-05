import sys
from inventory.inventory import Inventory
from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter
from importer.xml_importer import XmlImporter

if sys.argv[2] != "simples" and sys.argv[2] != "completo":
    raise ValueError("Argumento 2 inválido")

if sys.argv[1].endswith(".csv"):
    print(Inventory(CsvImporter).import_data(sys.argv[1], sys.argv[2]))
elif sys.argv[1].endswith(".json"):
    print(Inventory(JsonImporter).import_data(sys.argv[1], sys.argv[2]))
elif sys.argv[1].endswith(".xml"):
    print(Inventory(XmlImporter).import_data(sys.argv[1], sys.argv[2]))
else:
    raise ValueError("Argumento 1 inválido")
