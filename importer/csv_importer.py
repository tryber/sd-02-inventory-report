from importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(self, arq_name):
        with open(f"data/{arq_name}") as file:
            content = csv.reader(file, delimiter=",")
            header, *data = content
            report_list = []
            for item in data:
                report_list.append(
                    {
                        "id": item[0],
                        "nome_do_produto": item[1],
                        "nome_da_empresa": item[2],
                        "data_de_fabricacao": item[3],
                        "data_de_validade": item[4],
                        "numero_de_serie": item[5],
                        "instrucoes_de_armazenamento": item[5],
                    }
                )
        return report_list
