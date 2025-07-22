def filter_by_state(dictionaries: list, state: str) -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""

    new_dictionaries = []
    for dictionary in dictionaries:
        if dictionary.get("state") == state:
            new_dictionaries.append(dictionary)
    return new_dictionaries


def sort_by_date(dictionaries_data: list) -> list:
    """Функция возвращает новый список, отсортированный по дате"""

    sorted_dictionaries_data = sorted(dictionaries_data, key=lambda x: x["date"], reverse=True)
    return sorted_dictionaries_data
