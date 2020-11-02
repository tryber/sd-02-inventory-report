from helpers.constants import (EXPECTED_COMPLETE_REPORT,
                               EXPECTED_SIMPLE_REPORT, PATH_VALID_CSV, PATH_VALID_JSON, PATH_VALID_XML)
from inventory.inventory import Inventory


def test_csv_complete_report_on_success():
    complete_report = Inventory.import_data(PATH_VALID_CSV, "completo")
    assert complete_report == EXPECTED_COMPLETE_REPORT


def test_json_complete_report_on_success():
    complete_report = Inventory.import_data(PATH_VALID_JSON, "completo")
    assert complete_report == EXPECTED_COMPLETE_REPORT


def test_xml_complete_report_on_success():
    complete_report = Inventory.import_data(PATH_VALID_XML, "completo")
    assert complete_report == EXPECTED_COMPLETE_REPORT


def test_csv_simple_report_on_success():
    simple_report = Inventory.import_data(PATH_VALID_CSV, "simples")
    assert simple_report == EXPECTED_SIMPLE_REPORT


def test_json_simple_report_on_success():
    simple_report = Inventory.import_data(PATH_VALID_JSON, "simples")
    assert simple_report == EXPECTED_SIMPLE_REPORT


def test_xml_simple_report_on_success():
    simple_report = Inventory.import_data(PATH_VALID_XML, "simples")
    assert simple_report == EXPECTED_SIMPLE_REPORT
