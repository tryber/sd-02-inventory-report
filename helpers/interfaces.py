from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter
from importer.xml_importer import XmlImporter
from reports.complete_report import CompleteReport
from reports.simple_report import SimpleReport
from inventory.interface_interator import InterfaceInterator

IMPORTER = {
    "csv": CsvImporter,
    "json": JsonImporter,
    "xml": XmlImporter,
}

REPORT_TYPE = {
    "simples": SimpleReport,
    "completo": CompleteReport,
    "detalhado": InterfaceInterator
}
