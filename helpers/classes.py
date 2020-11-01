class Check:
    @classmethod
    def check_element(cls, element, available_elements, error_message=""):
        if element not in available_elements:
            raise ValueError(error_message)
