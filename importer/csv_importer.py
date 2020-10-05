from importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if not file.endswith(".csv"):
            raise ValueError("Extensão de arquivo inválida")
        products = []
        with open(file) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
            for row in reader:
                product = {}
                for key, value in dict(row).items():
                    if key == "id":
                        product[key] = int(value)
                    else:
                        product[key] = value
                products.append(product)
        return products
