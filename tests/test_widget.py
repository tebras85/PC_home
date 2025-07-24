import pytest
from src.widget import get_mask_account, mask_accoud_card

@pytest.mark.parametrize ('card_number, expected' , [('Visa Platinum 1111222233334444' , 'Visa Platinum 1111 22** **** 4444'),
                                                     ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                                     ('Master Card 7000792289606300', 'Master Card 7000 79** **** 6300'),
                                                     ('Счет 73654108430135874305' , 'Счет **4305' ),
                                                     ('Счет 73654108430135874399' , 'Счет **4399')
                                                     ])


def test_mask_accoud_card(card_number, expected):
    '''
    тест корректности маскировки карты
    '''
    assert mask_accoud_card(card_number) == expected