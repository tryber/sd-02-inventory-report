from abc import ABC, abstractmethod
import os.path


class Importer(ABC):
    @abstractmethod
    def import_data():
        raise NotImplementedError

    @classmethod
    def compare_type(cls, file_type, path_to_file):
        extension = os.path.splitext(path_to_file)[1]
        if file_type != extension:
            raise ValueError
