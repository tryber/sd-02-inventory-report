from importer.csv_importer import CsvImporter
from helpers.constants import (
    EXPECTED_DATA, PATH_INVALID_EXTENSION, PATH_NOT_EXIST, PATH_VALID_CSV
)

import pytest


def test_csv_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="File not found"):
        CsvImporter.import_data(PATH_NOT_EXIST)


def test_csv_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Invalid extension"):
        CsvImporter.import_data(PATH_INVALID_EXTENSION)


def test_csv_importer_on_success():
    receive_data = CsvImporter.import_data(PATH_VALID_CSV)
    assert receive_data == EXPECTED_DATA
