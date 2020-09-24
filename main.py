from inventory.inventory import Inventory
import sys

try:
    print(Inventory.import_data('data/inventory_20200823.xml', 'simples'))

except KeyError:
    print("Tipo de arquivo inválido", file=sys.stderr)
    sys.exit(1)
