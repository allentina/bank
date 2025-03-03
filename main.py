from src.masks import mask_card_number, mask_account_number


def main() -> None:
    card_number = "1234567890123456"
    masked_card = mask_card_number(card_number)
    print("Masked card:", masked_card)

    account_number = "9876543210"
    masked_account = mask_account_number(account_number)
    print("Masked account:", masked_account)


if __name__ == "__main__":
    main()
