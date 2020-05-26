from itertools import zip_longest
from items.abstract_item import Item


def introduce_from_list(list_: iter, space=False) -> None:
    print()
    if space:
        for number, action in enumerate(list_, start=1):
            print(number, action)
            print()
    else:
        for number, action in enumerate(list_, start=1):
            print(number, action)
    print()


def choose_item(items: iter, question: str):
    choices_actions = {str(number): item for number, item in enumerate(items, start=1)}
    while True:
        try:
            if (choice := input(question)) != "":
                return choices_actions[choice]
            return None
        except KeyError:
            print("\nPodana wartość jest nieprawidłowa, spróbuj jeszcze raz!\n")


def get_classes_from_keys(dict_: dict) -> list:
    return [item for item in dict_.keys()]


def classes_to_items(list_of_classes: list) -> list:
    return [item() for item in list_of_classes]


def count_class_occurances(list_of_classes: list, names_set: set) -> dict:
    class_occurances = {}
    list_of_names = list(names_set)
    list_of_names.sort()
    for class_name in list_of_names:
        count = 0
        for cls in list_of_classes:
            if cls.__str__() == class_name:
                count += 1
        class_occurances[class_name] = count
    return class_occurances


def string_objects_representation(object_represantation):
    string = ""
    if type(object_represantation) == list:
        for number, object in enumerate(object_represantation):
            left = f'{number} - '.split('\n')
            right = str(object).split('\n')
            for line in zip_longest(left, right, fillvalue=' '*len(left[0])):
                string += "".join(list(line)) + "\n"
        return string
