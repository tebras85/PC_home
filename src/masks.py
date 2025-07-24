def get_mask_card_number(card_number: str) -> str:
    """
    Делаем маску номера карты , скрывая некоторые цифры номера карты.
    """
    if len(card_number) < 16 or len(card_number) > 16:
        return  'не корректно введены данные!!!'
    return card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]

def get_mask_account(card_account: str) -> str:
    """
    Выводим последние цифры номера счета клиента
    """
    if len(card_account) == 0:
        return 'не корректно введены данные!!!'
    card_account = card_account.replace(" ", "")
    last_part = str(card_account[-4:])
    return f"**{last_part}"


if __name__ == '__main__':

    print(get_mask_card_number('123456'))
    print(get_mask_card_number('1111222233334444'))
    print(get_mask_account('1111222233334444'))
    print(get_mask_account(''))