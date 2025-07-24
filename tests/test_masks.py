import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected",
                        [("7000792289606361", "7000 79** **** 6361"),
                        ("7000792289606745", "7000 79** **** 6745"),
                        ("7220792289606798", "7220 79** **** 6798")])
def test_masks(card_number: str, expected: str)-> str:
    """
    тест корректности маскировки карты
    """
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number,", [("70007922896063610"),
                                          ("70007922896067450"),
                                          ("722079228960679"),
                                          ("32")])
def test_masks_type(card_number: str)-> str:
    """
    тест корректности ввода номера карты 16 символов
    """
    assert get_mask_card_number(card_number) == "не корректно введены данные!!!"


@pytest.mark.parametrize("account, expected",
                            [("7000792289606361", "**6361"),
                            ("7000792289606745", "**6745"),
                            ("7220792289606798", "**6798")])
def test_get_mask_account(account: str, expected: str)-> str:
    """
    тест корректности маскировки счета
    """
    assert get_mask_account(account) == expected


def test_get_mask_account_zero()-> str:
    """
    тест на пустую строку
    """
    assert get_mask_card_number("") == "не корректно введены данные!!!"
