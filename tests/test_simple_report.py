from reports.simple_report import SimpleReport
from helpers.constants import (EXPECTED_DATA, EXPECTED_SIMPLE_REPORT)


def test_simple_report_on_success():
    simple_report = SimpleReport.generate(EXPECTED_DATA)
    assert simple_report == EXPECTED_SIMPLE_REPORT
