from helpers.functions import get_extension
from helpers.interfaces import (IMPORTER, REPORT_TYPE)


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        extension = get_extension(file_path)
        file_data = IMPORTER[extension].import_data(file_path)
        return REPORT_TYPE[report_type].generate(file_data)
