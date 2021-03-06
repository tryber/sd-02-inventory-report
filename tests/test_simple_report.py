from helpers.constants import (EXPECTED_DATA, EXPECTED_SIMPLE_REPORT)
from reports.simple_report import SimpleReport


def test_simple_report_on_success():
    simple_report = SimpleReport.generate(EXPECTED_DATA)
    print(simple_report)
    assert simple_report == EXPECTED_SIMPLE_REPORT
