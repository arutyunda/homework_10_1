def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """принимает список словарей и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению"""

    filtered_list = []
    for dict in list_of_dicts:
        if dict.get("state") == state:
            filtered_list.append(dict)
    return filtered_list


# проверка работы функции
# dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#
# filtered_list = filter_by_state(dict, state ='CANCELED')
#
# for dict in filtered_list:
#     print(f'{dict}')
