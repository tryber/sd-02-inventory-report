from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, report_type, class_importer, arquive):

        file_to_report = class_importer.import_data(arquive)

        if report_type == "simple":
            return SimpleReport.generate(file_to_report)
        if report_type == "complete":
            return CompleteReport.generate(file_to_report)
