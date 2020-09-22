from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory():
    @classmethod
    def import_data(cls, type, arquive):
        if (type == 'simple'):
            return SimpleReport.generate(arquive)
        if (type == 'complete'):
            return CompleteReport.generate(arquive)

