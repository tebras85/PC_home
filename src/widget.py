from src.masks import get_mask_account, get_mask_card_number


def mask_accoud_card(info: str) -> str:
    """обрабатывает информацию о картах и счетах, выводит замаскированный номер"""
    parts = info.split()
    type_info = " ".join(parts[:-1])
    number = parts[-1]

    if parts[0].lower() in "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{type_info} {masked_number}"


def get_date(user_data: str) -> str:
    """Функция переформатирует дату"""
    data_user = user_data.split("T")
    data = "".join(data_user[0])
    data_format = data.split("-")
    day = data_format[2]
    month = data_format[1]
    year = data_format[0]
    return f'"{day}.{month}.{year}"'

