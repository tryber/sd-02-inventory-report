from datetime import date
import statistics


class SimpleReport:
    @classmethod
    def generate(cls, produtos):
        datas_de_fabricacao = [
            produto["data_de_fabricacao"]
            for produto in produtos
        ]
        fabricacao_mais_antiga = min(datas_de_fabricacao)

        datas_de_validade = [
            produto["data_de_validade"]
            for produto in produtos
            if produto["data_de_validade"] >= date.today().strftime("%Y-%m-%d")
        ]
        validade_mais_proxima = min(datas_de_validade)

        lista_de_empresas_para_cada_produto = [
            produto["nome_da_empresa"]
            for produto in produtos
        ]
        empresa_que_aparece_mais_vezes = statistics.mode(lista_de_empresas_para_cada_produto)

        return f"""
Data de fabricação mais antiga: {fabricacao_mais_antiga}
Data de validade mais próxima: {validade_mais_proxima}
Empresa com maior quantidade de produtos estocados: {empresa_que_aparece_mais_vezes}
        """
