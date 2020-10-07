from importer.importer import Importer
from unittest.mock import patch


@patch('importer.importer.Importer.compare_type')
def test_compare_type(mocker):
    Importer.compare_type('file_type', 'tests/arquivo_mock.txt')

