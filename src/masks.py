def get_mask_card_number(card_number: str) -> str:
    """
    Делаем маску номера карты , скрывая некоторые цифры номера карты.
    """
    if len(card_number) < 16 or len(card_number) > 16:
        return 'Не коректный вод карты!!! '
    #formatted_number = card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]
    #return formatted_number
    return card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]

def get_mask_account(card_account: str) -> str:
    """
    Выводим последние цифры номера счета клиента
    """
    card_account = card_account.replace(" ", "")
    last_part = str(card_account[-4:])
    return f"**{last_part}"
