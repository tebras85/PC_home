from src.masks import get_mask_account, get_mask_card_number

card_number = get_mask_card_number("7000792289606361")
print(card_number)

mask_account = get_mask_account("234576543270986")
print(mask_account)
