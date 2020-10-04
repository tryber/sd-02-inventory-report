from reports.simple_report import SimpleReport
from tests.mock_received_list import mock_received_list


class TestSimpleReportGenerate:
    def test_date_fab(self):
        expect = "Data de fabricação mais antiga: 2020-05-31"
        assert expect in SimpleReport.generate(mock_received_list)


    def test_date_valid(self):
        expect = "Data de validade mais próxima: 2023-01-17"
        assert expect in SimpleReport.generate(mock_received_list)


    def test_enterprise_greater_occurencies(self):
        expect = "Empresa com maior quantidade de produtos estocados: sanofi-aventis U.S. LLC"
        assert expect in SimpleReport.generate(mock_received_list)


def test_get_most_frequent_enterprise():
    expect_enterprise_name = "sanofi-aventis U.S. LLC"

    received = SimpleReport.get_most_frequent_enterprise(mock_received_list)

    assert expect_enterprise_name == received


def test_get_occurrence_count():
    expect_enterprise_occurrences = [
      {"empresa": "Forces of Nature", "ocorrencias": 1 },
      {"empresa": "sanofi-aventis U.S. LLC", "ocorrencias": 2 },
    ]

    received = SimpleReport.get_occurrence_count(mock_received_list)

    assert expect_enterprise_occurrences == received
