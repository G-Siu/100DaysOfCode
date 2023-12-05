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
            line.append((item["description"][:23].ljust(23)
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
    # Get amounts from each category
    ledgers = [item.ledger for item in categories]

    # Pick out amounts in each category ledger
    amounts = list()
    for ledger in ledgers:
        amounts.append([item["amount"] for item in ledger])

    # Total positive and negative balances in each category
    # positives = list()
    negatives = list()
    for amount in amounts:
        # positives.append(sum(item for item in amount if str(item)[0] != "-"))
        negatives.append(-sum(item for item in amount if str(item)[0] == "-"))
    # Percentage of total spent in each category
    percentages = list()
    total_negatives = sum(negatives)
    try:
        for i in range(len(negatives)):
            # Height of each bar is rounded down to nearest 10
            percentages.append(round_down((negatives[i]
                                           / total_negatives) * 100, 10))
    except ValueError:
        percentages.append(0)
    chart_line = list()
    # Title top of chart
    chart_line.append("Percentage spent by category\n")
    # Y-axis labeled 0-100, increments of 10
    for label in range(100, -1, -10):
        chart_line.append(f"{label}|".rjust(4))
        # 'Bars' are represented as 'o'
        for i in range(len(percentages)):
            if percentages[i - 1] < label <= percentages[i]:
                chart_line[-1] += (" " * 3) * i + " o "
            elif percentages[i] >= label:
                chart_line[-1] += " o "

        chart_line[-1] += "\n"
    # Dashed horizontal line goes two characters past the final bar
    chart_line.append((" " * 4) + ("-" * 3) * len(categories) + "-\n")
    # Category vertically displayed
    vertical_words = list()
    count = -1  # To get empty spaces in the previous category column
    for words in categories:
        count += 1
        word = words.category
        # List each letter
        vertical_word = [f" {v} " for i, v in enumerate(word)]
        lengths = len(vertical_words)
        length = len(vertical_word)
        # Starts with first word in first column
        if not vertical_words:
            vertical_words = [" " * 4 + letter for letter in vertical_word]
        elif length > lengths:
            # Add empty spaces in place of column if no letter
            for i in range(1, lengths):
                if len(vertical_words[i]) != len(vertical_words[i - 1]):
                    vertical_words[i] += " " * 3
            # Add letter as normal
            for i in range(lengths):
                vertical_words[i] = vertical_words[i] + vertical_word[i]
            # Add space if new line with no letter in first column
            for i in range(lengths, length):
                vertical_words.append(" " * 4 + "   " * count +
                                      vertical_word[i])
        else:
            for i in range(len(vertical_word)):
                vertical_words[i] = vertical_words[i] + vertical_word[i]
    for column in range(len(vertical_words) - 1):
        vertical_words[column] += " \n"

    # Combine chart sections
    chart_line.extend(vertical_words)
    return "".join(chart_line)


# Function to round down to nearest 10
def round_down(num, div):
    return num - (num % div)
