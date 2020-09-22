import datetime
from itertools import groupby
from operator import itemgetter


class SimpleReport:
    @classmethod
    def generate(cls, received_list):
        list_date_fab = [
            datetime.date.fromisoformat(item['data_de_fabricacao'])
            for item in received_list]
        list_date_fab.sort()
        list_date_val = [
            datetime.date.fromisoformat(item['data_de_validade'])
            for item in received_list]
        list_date_val.sort()
        enterprise_name = cls.get_most_frequent_enterprise(received_list)
        return f"""
Data de fabricação mais antiga: {list_date_fab[0]}
Data de validade mais próxima: {list_date_val[0]}
Empresa com maior quantidade de produtos estocados: {enterprise_name}"""

    @classmethod
    def get_most_frequent_enterprise(cls, received_list):
        return max(
            cls.get_occurrence_count(received_list),
            key=itemgetter('ocorrencias'))['empresa']

    @classmethod
    def get_occurrence_count(cls, received_list):
        enterprises = [item['nome_da_empresa'] for item in received_list]
        enterprises.sort()
        return [{'empresa': key,
                'ocorrencias': len(list(group))} for (key,
                group) in groupby(enterprises)]
