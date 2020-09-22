import datetime
from itertools import groupby
import operator


class SimpleReport:
    @classmethod
    def generate(cls, received_list):
        list_data = [
            datetime.date.fromisoformat(item['data_de_fabricacao'])
            for item in received_list]
        list_data.sort()
        print(f'Data de fabricação mais antiga: {list_data[0]}')
        list_data = [
            datetime.date.fromisoformat(item['data_de_validade'])
            for item in received_list]
        list_data.sort()
        print(f'Data de validade mais próxima: {list_data[0]}')
        print(f'Empresa com maior quantidade de produtos estocados: \
{cls.get_most_quantity_enterprise(received_list)}')

    @classmethod
    def get_most_quantity_enterprise(cls, received_list):
        enterprises = [item['nome_da_empresa'] for item in received_list]
        enterprises.sort()
        most_frequent_enterprise = [{'empresa': key,
                                    'ocorrencias': len(list(group))} for (key,
                                    group) in groupby(enterprises)]
        return max(
            most_frequent_enterprise,
            key=operator.itemgetter('ocorrencias'))['empresa']
