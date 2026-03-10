import re


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        self.ledger.append({"amount": -amount, "description": description})

        if self.check_funds(amount):
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance

    def transfer(self, amount, category):
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")

        if self.check_funds(amount):
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        output = ""
        n_max = 30

        n_s = (n_max - len(self.name)) // 2
        title = f"{n_s * '*'}{self.name}{n_s * '*'}"
        output += title
        # print(title)

        for entry in self.ledger:
            amount = f"{entry['amount']:.2f}"
            description = entry["description"]

            n_a = len(amount)
            n_a_max = 7
            if n_a > n_a_max:
                amount = amount[: n_a_max - 3] + "..."
                n_a = len(amount)

            n_d = len(description)
            n_d_max = n_max - n_a - 1
            if n_d > n_d_max:
                description = description[:n_d_max] + " "

            n_sp = n_max - n_d - n_a

            entry = f"\n{description}{n_sp * ' '}{amount}"
            output += entry
            # print(entry)
            # print(n_max, n_d)

        balance = f"\nTotal: {self.get_balance()}"
        output += balance
        # print(balance)

        return output
        # return str(self.ledger)


def create_spend_chart(categories):
    def match_categories(description):
        categs = {
            "Auto": r"(car|auto)s?",
            "Clothing": r"cloth(es|ing)",
            "Food": r"food|grocer(y|ies)|restaurant",
        }

        for key, pattern in categs.items():
            if re.search(pattern, description, re.IGNORECASE):
                return key
        return "Misc"

    categs = {}
    chart = "Percentage spent by category"

    totals = []
    for cat in categories:
        spent = sum(entry["amount"] for entry in cat.ledger if entry["amount"] < 0)
        totals.append(spent)

    grand_total = sum(totals)
    percentages = [t / grand_total * 100 for t in totals]

    for y in range(100, -10, -10):
        chart += f"\n{y:3}|"
        for p in percentages:
            chart += " o " if p >= y else "   "
        chart += " "

    chart += "\n    " + "-" + "-" * (3 * len(categories))

    labels = [cat.name for cat in categories]
    max_len = max(len(l) for l in labels)
    for i in range(max_len):
        chart += "\n    "
        for l in labels:
            chart += f" {l[i] if i < len(l) else ' '} "
        chart += " "

    return chart


def main():
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category("Clothing")
    food.transfer(50, clothing)

    print(food)
    print(create_spend_chart([food, clothing]))


main()
