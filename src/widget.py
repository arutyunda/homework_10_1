from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
    """Маскирует тип и номер карты или счета"""

    prefix = ""
    for symbol in user_data:
        if not symbol.isdigit():
            prefix += symbol

    numbers = user_data.split()[-1]
    if len(str(numbers)) == 16:
        return prefix + str(get_mask_card_number(int(numbers)))
    if len(str(numbers)) == 20:
        return prefix + str(get_mask_account(int(numbers)))
    else:
        return "Неверно ввели номер"


def get_date(date: str) -> str:
    """возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""

    YYYY = date[:4]
    MM = date[5:7:]
    DD = date[8:10:]
    formatted_date = f"{DD}.{MM}.{YYYY}"
    return formatted_date


# list = [
#     mask_account_card("Maestro 1596837868705199"),
#     mask_account_card("Счет 64686473678894779589"),
#     mask_account_card("MasterCard 7158300734726758"),
#     mask_account_card("Счет 35383033474447895560"),
#     mask_account_card("Visa Classic 6831982476737658"),
#     mask_account_card("Visa Platinum 8990922113665229"),
#     mask_account_card("Visa Gold 5999414228426353"),
#     mask_account_card("Счет 73654108430135874305"),
# ]
#
# for item in list:
#     print(item)
#
# date = "2024-03-11T02:26:18.671407"
# print("\n" + get_date(date))
