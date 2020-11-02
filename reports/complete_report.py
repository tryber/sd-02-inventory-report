from helpers.functions import get_elements
from reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)
        companies = get_elements(data, "nome_da_empresa")
        companies_set = sorted(set(companies))
        products_by_company = ["- " + str(company) + ": " + str(
            companies.count(company)) for company in companies_set]
        complete_report = "\n".join(products_by_company)
        return """{}
Produtos estocados por empresa:
{}
""".format(simple_report, complete_report)
