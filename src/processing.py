def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """принимает список словарей и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению"""

    filtered_list = []
    for dict in list_of_dicts:
        if dict.get("state") == state:
            filtered_list.append(dict)
    return filtered_list


def sort_by_date(list_of_dicts: list, order: bool = True) -> list:
    """принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    и возвращает новый список, отсортированный по дате"""

    list_of_dicts = sorted(list_of_dicts, reverse=order, key=lambda list_of_dicts: list_of_dicts["date"])
    return list_of_dicts


# проверка работы функций

# dict1 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# dict2 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# filtered_by_state = filter_by_state(dict1, state ='CANCELED')
# for dict in filtered_by_state:
#     print(f'{dict}')
#
# print()
#
# sorted_by_date = sort_by_date(dict2, order=False)
# for dict in sorted_by_date:
#     print(dict)
