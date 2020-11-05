from helpers.classes import Check
from helpers.constants import (
    AVAILABLE_EXTENSIONS, AVAILABLE_TYPES,
    ERROR_ARGUMENTS, ERROR_EXTENSION, ERROR_TYPE
)
from helpers.functions import get_extension
from inventory.inventory import Inventory

import sys


def main(file_path, report_type):

    extension = get_extension(file_path)
    Check.check_element(extension, AVAILABLE_EXTENSIONS, ERROR_EXTENSION)
    Check.check_element(report_type, AVAILABLE_TYPES, ERROR_TYPE)

    Inventory.import_data(file_path)
    if report_type != "detalhado":
        print(Inventory.get_report(report_type))
    else:
        Inventory.__iter__(report_type)


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        report_type = sys.argv[2]
    except IndexError:
        raise ValueError(ERROR_ARGUMENTS)
    else:
        main(file_path, report_type)
