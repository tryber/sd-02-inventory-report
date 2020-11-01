from helpers.classes import Check
from helpers.constants import (
    AVAILABLE_EXTENSIONS, AVAILABLE_TYPES,
    ERROR_ARGUMENTS, ERROR_EXTENSION, ERROR_TYPE
)
from helpers.functions import get_extension
import sys


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        report_type = sys.argv[2]
        extension = get_extension(file_path)
        Check.check_element(extension, AVAILABLE_EXTENSIONS, ERROR_EXTENSION)
        Check.check_element(report_type, AVAILABLE_TYPES, ERROR_TYPE)
    except IndexError:
        raise ValueError(ERROR_ARGUMENTS)
    else:
        raise NotImplementedError
