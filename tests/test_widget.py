import pytest

from src.widget import get_date, mask_accoud_card


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("Visa Platinum 1111222233334444", "Visa Platinum 1111 22** **** 4444"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Master Card 7000792289606300", "Master Card 7000 79** **** 6300"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 73654108430135874399", "Счет **4399"),
    ],
)
def test_mask_accoud_card(card_number: str, expected: str) -> str:
    """
    тест корректности маскировки карты
    """
    assert mask_accoud_card(card_number) == expected


@pytest.mark.parametrize("card_number", [("111222233334444"), ("70007922896067450"), ("722079228960679"), ("32432")])
def test_mask_accoud_card_n(card_number):
    """
    тест корректности ввода номера карты 16 символов
    """
    assert mask_accoud_card(card_number) == " не корректно введены данные!!!"


@pytest.mark.parametrize(
    "data, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-03-11T02:26:18.671407", "11.03.2023"),
        ("2025-04-11T02:26:00.671407", "11.04.2025"),
    ],
)
def test_get_date(data: str, expected: str) -> str:
    """
    тест корректности даты
    """
    assert get_date(data) == expected
