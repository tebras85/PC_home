def get_mask_card_number(card_number: str) -> str:
    """
    Делаем маску номера карты , скрывая некоторые цифры номера карты.
    """

    mask_card_number = card_number.replace(card_number[7:12], "******")
    formatted_number = (
        mask_card_number[:4] + " " + mask_card_number[5:9] + " " + mask_card_number[8:12] + " " + mask_card_number[-4:]
    )
    return formatted_number


def get_mask_account(card_account: str) -> str:
    """
    Выводим последние цифры номера счета клиента
    """
    card_account = card_account.replace(" ", "")
    last_part = str(card_account[-4:])
    return f"**{last_part}"
