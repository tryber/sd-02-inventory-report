from reports.complete_report import CompleteReport
from tests.mock_received_list import mock_received_list


def test_generate():
    expect = """
Data de fabricação mais antiga: 2020-05-31
Data de validade mais próxima: 2023-01-17
Empresa com maior quantidade de produtos estocados: sanofi-aventis U.S. LLC
Produtos estocados por empresa:
- Forces of Nature: 1
- sanofi-aventis U.S. LLC: 2"""
    received = CompleteReport.generate(mock_received_list)

    assert expect == received


def test_get_occurrence_count_child():
    expect = """
Produtos estocados por empresa:
- Forces of Nature: 1
- sanofi-aventis U.S. LLC: 2"""

    received = CompleteReport.get_occurrence_count_child(mock_received_list)

    assert expect == received
