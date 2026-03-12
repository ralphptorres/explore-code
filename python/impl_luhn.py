def verify_card_number(card_number: str):
    card_number = card_number.replace(" ", "").replace("-", "")
    total = sum(
        (2 * int(d) - 9)
        if i % 2 and 2 * int(d) > 9
        else (2 * int(d))
        if i % 2
        else int(d)
        for i, d in enumerate(card_number[::-1])
    )

    return "VALID!" if not total % 10 else "INVALID!"


print(verify_card_number("453914881"))
print(verify_card_number("1234 5678 9012 3456"))
