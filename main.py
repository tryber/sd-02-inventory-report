import sys
from inventory.inventory import Inventory

if len(sys.argv) != 3:
    print('Verifique os argumentos')
else:
    print(Inventory.import_data(sys.argv[1], sys.argv[2]))
