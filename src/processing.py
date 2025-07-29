def filter_by_state(dictionaries: list, state: str) -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""

    #new_dictionaries = []
    #for dictionary in dictionaries:
    #    if dictionary.get("state") == state:
    #        new_dictionaries.append(dictionary)
    #return new_dictionaries
    return [x for x in dictionaries if x.get("state") == state]

def sort_by_date(dictionaries_data: list) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_dictionaries_data = [x for x in dictionaries if x.get('date')]
    #sorted_dictionaries_data = sorted(dictionaries_data, key=lambda x: x["date"], reverse=True)
    #return sorted_dictionaries_data
    return sorted(sorted_dictionaries_data, key=lambda x: x["date"], reverse=True)


if __name__  == '__main__':

    dictionaries = [{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED'}]

    print(filter_by_state(dictionaries, state='EXECUTED'))

    print(sort_by_date(dictionaries))