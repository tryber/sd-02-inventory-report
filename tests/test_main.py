from main import main
from helpers.constants import (
    PATH_INVALID_EXTENSION, PATH_VALID_CSV, EXPECTED_SIMPLE_REPORT, EXPECTED_COMPLETE_REPORT, EXPECTED_DETAILS, EXPECTED_DETAILS_PREVIOUS, EXPECTED_DETAILS_NEXT)
import pytest
from unittest.mock import patch, Mock


def test_main_on_invalid_extension():
    with pytest.raises(ValueError, match="Invalid extension"):
        main(PATH_INVALID_EXTENSION, "")


def test_main_on_invalid_type():
    with pytest.raises(ValueError, match="Report type doesn't available"):
        main(PATH_VALID_CSV, "not_exist_type")


def test_main_on_simple_riport(capsys):
    main(PATH_VALID_CSV, "simples")
    out, err = capsys.readouterr()
    assert out == EXPECTED_SIMPLE_REPORT + "\n"


def test_main_on_details(capsys):
    with patch("inventory.interface_interator.inquirer") as mock_inquirer:
        mock_inquirer.List.return_value = ""
        mock_inquirer.prompt.return_value = {"option": "Exit"}
        main(PATH_VALID_CSV, "detalhado")
        out, err = capsys.readouterr()
        assert out == EXPECTED_DETAILS + "\n"


def test_main_on_details_next(capsys):
    with patch("inventory.interface_interator.inquirer") as mock_inquirer:
        mock_inquirer.List.return_value = ""
        mock_inquirer.prompt = Mock()
        mock_inquirer.prompt.side_effect = [
            {"option": "Next"},  {"option": "Exit"}]
        main(PATH_VALID_CSV, "detalhado")
        out, err = capsys.readouterr()
        assert out == EXPECTED_DETAILS_NEXT + "\n"


def test_main_on_details_previous(capsys):
    with patch("inventory.interface_interator.inquirer") as mock_inquirer:
        mock_inquirer.List.return_value = ""
        mock_inquirer.prompt = Mock()
        mock_inquirer.prompt.side_effect = [
            {"option": "Previous"},  {"option": "Exit"}]
        main(PATH_VALID_CSV, "detalhado")
        out, err = capsys.readouterr()
        assert out == EXPECTED_DETAILS_PREVIOUS + "\n"


def test_main_on_complete_riport(capsys):
    main(PATH_VALID_CSV, "completo")
    out, err = capsys.readouterr()
    assert out == EXPECTED_COMPLETE_REPORT + "\n"
