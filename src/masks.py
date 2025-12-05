def get_mask_card_number(card_number_int: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX,
    где X — это цифра номера"""

    card_number_str = str(card_number_int)
    card_number_list: list[str] = []
    i = 0  # счетчик до 4, чтобы разделять номер карты на группы по 4 цифры
    k = 0  # счетчик, чтобы решить заменять цифру карты на * или нет
    item: str

    for item in card_number_str:
        i += 1
        k += 1
        if 6 < k <= len(card_number_str) - 4:
            card_number_list.append(item)
            if i == 4:
                card_number_list.append(" ")
                i = 0
        else:
            card_number_list.append("*")
            if i == 4:
                card_number_list.append(" ")
                i = 0
    return "".join(card_number_list)


def get_mask_account(account_int: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в формате **XXXX, где X — это цифра номера"""

    account_str = str(account_int)
    account_mask = f"**{account_str[-4:]}"
    return account_mask


# Далее код для проверки функций, в этом модуле он уже не нужен
#
# card_number_mask = get_mask_card_number(1234123412341234)
# print(card_number_mask)
#
# account_mask = get_mask_account(1234123412341234)
# print(account_mask)
