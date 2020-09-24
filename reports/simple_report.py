from datetime import datetime
from collections import Counter


class SimpleReport:
    def sort_report(self, param, report_list):
        def one_obj(obj):
            return obj[param]

        return sorted(report_list, key=one_obj)

    def compare_dates(self, sorted_report_list):
        today = datetime.now().strftime("%Y-%m-%d")
        for item in sorted_report_list:
            if item["data_de_validade"] > today:
                return item["data_de_validade"]

    def count_enterprises(self, report_list):
        dict_report = Counter(
            [item["nome_da_empresa"] for item in report_list]
        )
        return dict_report

    def generate(self, report_list):
        mfac = "data_de_fabricacao"
        valid = "data_de_validade"
        manufactory_date = self.sort_report(mfac, report_list)[0]
        validate_date = self.compare_dates(
            self.sort_report(valid, report_list)
        )
        enterp = self.count_enterprises(report_list).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {manufactory_date[mfac]}\n"
            f"Data de validade mais próximas: {validate_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {enterp}\n"
        )
