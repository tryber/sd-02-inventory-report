from datetime import datetime, date
from itertools import groupby
from operator import itemgetter


class SimpleReport:
    @classmethod
    def generate(cls, received_list):
        list_date_fab = [
            date.fromisoformat(item['data_de_fabricacao'])
            for item in received_list]
        list_date_fab.sort()

        list_date_val = [
            datetime.strptime(item['data_de_validade'], '%Y-%m-%d')
            for item in received_list]
        today = datetime.now().date()

        minimum = datetime.strptime('2300-10-10', '%Y-%m-%d').date()
        for d1 in list_date_val:
            if d1.date() > today and d1.date() < minimum:
                minimum = d1.date()

        enterprise_name = cls.get_most_frequent_enterprise(received_list)

        return f"""
Data de fabricação mais antiga: {list_date_fab[0]}
Data de validade mais próxima: {minimum}
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
