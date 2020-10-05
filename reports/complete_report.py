from reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, produtos):
        inherited_generate = super().generate

        lista_de_empresas_para_cada_produto = [
            produto["nome_da_empresa"]
            for produto in produtos
        ]
        dicionario_de_quantidade_de_produtos_por_empresa = Counter(lista_de_empresas_para_cada_produto)
        string_empresas_quantidades = "\n".join([
            f"- {key}: {value}"
            for key, value in dicionario_de_quantidade_de_produtos_por_empresa.items()
        ])

        more_information = f"""
Produtos estocados por empresa:
{string_empresas_quantidades}"""

        return inherited_generate(produtos) + more_information
