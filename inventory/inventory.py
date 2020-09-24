from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport


class Inventory:
    def __init__(self, conversor):
        self.conversor = conversor

    def import_data(self, dict_value, report_type):
        file_parsed = self.conversor.import_data(dict_value)

        if report_type == 'simples':
            return SimpleReport.generate(file_parsed)
        elif report_type == 'completo':
            return CompleteReport.generate(file_parsed)
        else:
            return "Tipo de relatório inexistente"
