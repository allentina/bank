from src.masks import mask_account_number

if __name__ == "__main__":
    card_num = 7000792289606361
    account_num = 73654108430135874305

    print("Маска карты:", mask_card_number(card_number))
    print("Маска счета:", mask_account_number(account_number))
