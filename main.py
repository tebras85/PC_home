from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_accoud_card

card_number = get_mask_card_number("7000792289606361")
print(card_number)

mask_account = get_mask_account("234576543270986")
print(mask_account)

accoud_card = mask_accoud_card('Visa Platinum 7000792289606361')
print(accoud_card)
