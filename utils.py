def introduce_from_list(list_: list) -> None:
    for number, action in enumerate(list_):
        print(number, action)


def choose_item(list_of_items: list, question: str) -> int:
    try:
        while True:
            choice = input(question)
            return list_of_items[int(choice)] if choice else None
    except ValueError:
        print("\nPodano nieprawidłowy numer, spróbuj jeszcze raz.\n")
