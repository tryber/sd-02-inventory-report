from helpers.constants import (EXPECTED_DATA, EXPECTED_COMPLETE_REPORT)
from reports.complete_report import CompleteReport


def test_complete_report_on_success():
    complete_report = CompleteReport.generate(EXPECTED_DATA)
    print(complete_report)
    assert complete_report == EXPECTED_COMPLETE_REPORT
