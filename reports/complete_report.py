from reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate_complete(cls, dict_file):
        string_complete = 'Produtos estocados por empresa:\n'

        products_by_industry = Counter(
            industry["nome_da_empresa"] for industry in dict_file)

        for item, quantity in products_by_industry.items():
            string_complete += (f'- {item}: {quantity}\n')

        return string_complete

    @classmethod
    def generate(cls, dict_file):
        string_simple = super().generate(dict_file)
        string_complete = cls.generate_complete(dict_file)
        return(string_simple + '\n' + string_complete)
