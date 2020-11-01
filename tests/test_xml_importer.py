from importer.xml_importer import XmlImporter
from helpers.constants import (
    EXPECTED_DATA, PATH_INVALID_EXTENSION, PATH_NOT_EXIST_XML, PATH_VALID_XML
)

import pytest


def test_xml_importer_arquivo_nao_existe():
    with pytest.raises(ValueError, match="File not found"):
        XmlImporter.import_data(PATH_NOT_EXIST_XML)


def test_xml_importer_extensao_invalida():
    with pytest.raises(ValueError, match="Invalid extension"):
        XmlImporter.import_data(PATH_INVALID_EXTENSION)


def test_xml_importer_on_success():
    receive_data = XmlImporter.import_data(PATH_VALID_XML)
    assert receive_data == EXPECTED_DATA
