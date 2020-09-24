from importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(self, arq_name):
        with open(f"data/{arq_name}") as fd:
            doc = xmltodict.parse(fd.read())
            report_list = []
            for item in doc["dataset"]["record"]:
                report_list.append(
                    {
                        "id": item["id"],
                        "nome_do_produto": item["nome_do_produto"],
                        "nome_da_empresa": item["nome_da_empresa"],
                        "data_de_fabricacao": item["data_de_fabricacao"],
                        "data_de_validade": item["data_de_validade"],
                        "numero_de_serie": item["numero_de_serie"],
                        "instrucoes_de_armazenamento": item[
                            "instrucoes_de_armazenamento"
                        ],
                    }
                )
        return report_list
