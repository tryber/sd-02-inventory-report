from inventory.inventory import Inventory
import sys

print(Inventory.import_data(sys.argv[1], sys.argv[2]))
