from items.abstract_item import Item


def introduce_from_list(list_: list) -> None:
    for number, action in enumerate(list_, start=1):
        print(number, action)
        print()


def choose_item(list_of_items: list, question: str) -> Item:
    while True:
        try:
            choice = input(question)
            return list_of_items[int(choice) - 1] if choice else None
        except (ValueError, IndexError):
            print("\nPodano nieprawidłowy numer, spróbuj jeszcze raz.\n")


def get_classes_from_keys(dict_: dict) -> list:
    return [item for item in dict_.keys()]


def classes_to_items(list_of_classes: list) -> list:
    return [item() for item in list_of_classes]


def set_of_names(list_of_classes: list):
    return set([cls.__str__() for cls in list_of_classes])


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
