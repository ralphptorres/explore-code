def verify_card_number(card_number: str):
    if " " in card_number:
        card_number = "".join(card_number.split(" "))

    if "-" in card_number:
        card_number = "".join(card_number.split("-"))

    sum = 0
    for i, d in enumerate(card_number[::-1]):
        if i % 2:
            d = 2 * int(d)
            if d > 9:
                d -= 9
        else:
            d = int(d)
        sum += d
    print(sum)

    if sum % 10:
        return "INVALID!"
    else:
        return "VALID!"


print(verify_card_number("453914881"))
print(verify_card_number("1234 5678 9012 3456"))
