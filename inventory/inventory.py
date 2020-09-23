from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
from importer.csv_importer import CsvImporter
from importer.json_importer import JsonImporter
from importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def generate_report(cls, file, request_type):
        if request_type == "simples":
            return SimpleReport.generate(file)
        if request_type == "completo":
            return CompleteReport.generate(file)

    @classmethod
    def import_data(cls, file, request_type):
        if file.endswith(".csv"):
            return cls.generate_report(
                CsvImporter.import_data(file), request_type
            )
        if file.endswith(".json"):
            return cls.generate_report(
                JsonImporter.import_data(file), request_type
            )
        if file.endswith(".xml"):
            return cls.generate_report(
                XmlImporter.import_data(file), request_type
            )
