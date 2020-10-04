from reports.simple_report import SimpleReport
from functools import reduce


class CompleteReport(SimpleReport):
    def generate_complete(self, report_list):
        concat_reports = reduce(
            lambda acc, item: acc + f" - {item[0]}: {item[1]} \n",
            self.count_enterprises(report_list).most_common(),
            "",
        )

        return (
            f"{self.generate(report_list)}"
            f"Produtos estocados por empresa: \n"
            f"{concat_reports}"
        )
