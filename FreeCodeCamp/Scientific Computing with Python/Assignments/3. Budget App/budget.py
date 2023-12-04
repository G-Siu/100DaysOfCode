class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    # Return budget when category is printed
    def __str__(self):
        # Center title of category between * characters of a 30 character line
        title_line = self.category.center(30, "*")
        line = list()
        total = 0
        # Ledger items. 23 characters of description displayed, then the amount
        for item in self.ledger:
            # Amount is right aligned, max 7 characters
            line.append((item["description"].ljust(23)
                         + "{0:.2f}".format(item["amount"]).rjust(7)
                         + "\n"))
            # Add amount for total
            total += item["amount"]
        combine = (f"{title_line}\n{"".join(line)}Total: "
                   f"{"{0:.2f}".format(total)}")
        return combine

    # Accepts an amount and description
    # If no description, default to empty string
    def deposit(self, amount, description=""):
        deposit_dict = dict()
        # {"amount": amount, "description": description}
        deposit_dict["amount"] = amount
        deposit_dict["description"] = description
        # Append object to ledger list
        self.ledger.append(deposit_dict)

    # Similar to deposit, but pass amount as into ledger as negative number
    def withdraw(self, amount, description=""):
        # Return True if withdrawal successful, or False if not
        if Category.check_funds(self, amount):
            withdraw_dict = dict()
            # {"amount": -amount, "description": description}
            withdraw_dict["amount"] = -amount
            withdraw_dict["description"] = description
            # Append object to ledger list
            self.ledger.append(withdraw_dict)
            return True
        else:
            return False

    # Returns current balance of budget category
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    # Accepts amount and another budget category as arguments
    def transfer(self, amount, category):
        # If insufficient funds to withdraw, nothing should be added to
        # either ledgers
        if Category.check_funds(self, amount):
            # Withdraw amount
            transfer_dict = dict()
            transfer_dict["amount"] = -amount
            # Add description "Transfer to [Destination Budget Category]"
            transfer_dict["description"] = "Transfer to " + category.category
            self.ledger.append(transfer_dict)
            recipient_dict = dict()
            # Deposit into the other budget category
            recipient_dict["amount"] = amount
            # Add description "Transfer from [Source Budget Category]"
            recipient_dict["description"] = (f"Transfer from "
                                             f"{self.category}")
            category.ledger.append(recipient_dict)
            # Return True if successful transfer
            return True
        else:
            return False

    # Accepts amount as argument, used by both Withdraw and Transfer methods
    def check_funds(self, amount):
        # Return False if amount is greater than budget category balance
        if amount > Category.get_balance(self):
            return False
        else:
            return True


# Takes list of categories as argument. Return a string as bar chart:
def create_spend_chart(categories):
    # Title top of chart
    title_line = "Percentage spent by category"
    # Get amounts from each category
    ledgers = [item.ledger for item in categories]
    amounts = list()
    positives = list()
    negatives = list()
    percentages = list()
    # Pick out amounts in each category ledger
    for ledger in ledgers:
        amounts.append([item["amount"] for item in ledger])
    # Total positive and negative balances in each category
    for amount in amounts:
        positives.append(sum(item for item in amount if str(item)[0] != "-"))
        negatives.append(-sum(item for item in amount if str(item)[0] == "-"))
    # return positives, negatives
    # Percentage spent in each category
    for positive, negative in positives, negatives:
        percentages.append(round((negative / positive) * 100, -1))
    return percentages
    # - Y-axis should be labeled 0-100, increments of 10
    for label in range(100, 0, -10):

    # - The 'bars' are made of represented as 'o'
    # - Height of each bar is rounded to nearest 10
    # round(percentage, -1)
    # - A dashed horizontal line should go two characters past the final bar
    # - Each category name should be vertically displayed below this line

