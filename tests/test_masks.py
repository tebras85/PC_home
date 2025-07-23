import pytest
from src.masks import get_mask_card_number

@pytest.mark.parametrize ('card_number, expected' , [('7000792289606361' , '7000 79** **** 6361'),
                                                     ('7000792289606745', '7000 79** **** 6745')])
def test_masks(card_number, expected):
    assert get_mask_card_number(card_number) == expected