from inventory.inventory import Inventory
from importer.xml_importer import XmlImporter


# print(Inventory.import_data('simple', 'data/inventory_20200823.xml'))

# print(Inventory.convert_xml_to_Dict('data/inventory_20200823.xml'))

# XmlImporter.import_data('data/inventory_20200823.xml')

print(
    Inventory.import_data(
        "complete", XmlImporter, "data/inventory_20200823.xml"
    )
)
