from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, received_list):
        string = super().generate(received_list)
        string += cls.get_occurrence_count_child(received_list)
        print(string)

    @classmethod
    def get_occurrence_count_child(cls, received_list):
        string = """
Produtos estocados por empresa:"""
        ocurrency = super().get_occurrence_count(received_list)
        for enterprise in ocurrency:
            (_, empresa), (_, quantity) = enterprise.items()
            string += f"""
- {empresa}: {quantity}"""
        return string
