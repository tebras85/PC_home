import pytest
from src.masks import get_mask_card_number

@pytest.mark.parametrize ('card_number, expected' , [('7000792289606361' , '7000 79** **** 6361'),
                                                     ('7000792289606745', '7000 79** **** 6745'),
                                                     ('7220792289606798', '7220 79** **** 6798')
                                                     ])
def test_masks(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize ('card_number,' , [('70007922896063610'),
                                            ('70007922896067450'),
                                            ('722079228960679'),
                                            ('32')
                                            ])

def test_masks_type(card_number):
    assert get_mask_card_number(card_number) ==  'не корректно введены данные!!!'
