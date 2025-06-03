from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_accoud_card

card_number = get_mask_card_number("7000792289606361")
print(card_number)

mask_account = get_mask_account("234576543270986")
print(mask_account)

accoud_card = mask_accoud_card('Visa Platinum 7000792289606361')
print(accoud_card)

accoud_card = mask_accoud_card('Счет 73654108430135874305')
print(accoud_card)

date = get_date("2024-03-11T02:26:18.671407")
print(date)