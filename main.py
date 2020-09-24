from inventory.inventory import Inventory

inventory = Inventory()
inventory.import_data()
iterator = iter(inventory)
first_item = next(iterator)
print(first_item)
