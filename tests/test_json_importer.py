from importer.json_importer import JsonImporter
from helpers.constants import (
    EXPECTED_DATA, PATH_INVALID_EXTENSION, PATH_NOT_EXIST_JSON, PATH_VALID_JSON
)

import pytest


def test_json_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="File not found"):
        JsonImporter.import_data(PATH_NOT_EXIST_JSON)


def test_json_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Invalid extension"):
        JsonImporter.import_data(PATH_INVALID_EXTENSION)


def test_json_importer_on_success():
    receive_data = JsonImporter.import_data(PATH_VALID_JSON)
    assert receive_data == EXPECTED_DATA
