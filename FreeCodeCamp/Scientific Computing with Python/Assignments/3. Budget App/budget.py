class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

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
    @classmethod
    def withdraw(cls):
        # With description

        # If no description, default to empty string

        # Append object to ledger list as:
        # {"amount": amount, "description": description}

        # Return True if withdrawal successful, or False if not
        pass

    # Returns current balance of budget category
    @classmethod
    def get_balance(cls):
        pass

    # Accepts amount and another budget category as arguments
    @classmethod
    def transfer(cls):
        # Withdraw amount

        # Add description "Transfer to [Destination Budget Category]"

        # Deposit into the other budget category

        # Add description "Transfer from [Source Budget Category]"

        # If insufficient funds to withdraw, nothing should be added to
        # either ledgers

        # Return True if successful transfer
        # Return False if not
        pass

    # Accepts amount as argument, used by both Withdraw and Transfer methods
    @classmethod
    def check_funds(cls):
        # Return False if amount is greater than budget category balance
        # Else Return True
        pass

# When budget is printed:
# - Center title of category between * characters of a 30 character line
# - List of items in ledger. First 23 characters of description is displayed,
# then the amount
# - Final line displaying category total


# Takes list of categories as argument.
def create_spend_chart(categories):
    # Return a string as bar chart:
    # - Percentage spent in each category passed into this function
    # - Percentage spent should only consider withdrawals
    # - Y-axis should be labeled 0-100, increments of 10
    # - The 'bars' are made of represented as 'o'
    # - Height of each bar is rounded to nearest 10
    # - A dashed horizontal line should go two characters past the final bar
    # - Each category name should be vertically displayed below this line
    # - Title at top should say "Percentage spent by category"
    pass
