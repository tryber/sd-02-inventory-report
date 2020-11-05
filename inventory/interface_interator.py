from inventory.inventory_iterator import InventoryIterator
import inquirer

choices = [
    "Next",
    "Previous",
    "Exit"
]


def exit_code():
    pass


def prompt_next(iterator, data):
    print(iterator.__next__())
    main(data, iterator)


def prompt_previous(iterator, data):
    print(iterator.__previous__())
    main(data, iterator)


interface = {
    "Next": prompt_next,
    "Previous": prompt_previous,
    "Exit": exit_code,
}


def main(data, iterator):
    questions = [inquirer.List(
        "option", message="Selecione uma das opções a seguir", choices=choices)
    ]

    index = inquirer.prompt(questions)["option"]

    if index == "Exit":
        interface[index]
    else:
        interface[index](iterator, data)


class InterfaceInterator:
    @classmethod
    def __iter__(cls, data):
        iterator = InventoryIterator(data)
        print(iterator.__next__())
        main(data, iterator)
