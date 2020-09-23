from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
import json

# daqui pra baixo tem q ser removido, se quiser deixar automatizado


with open('data/inventory_20200823.json') as json_file:
    data = json.load(json_file)

print("\nComplete Report\n\n")
CompleteReport.generate(data)
