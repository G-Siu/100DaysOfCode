# Learn Lambda Functions by Building an Expense Tracker
# Name: G Siu
# Date created: 21st December 2023
# Date modified: 21st December 2023

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})


def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')


def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))


def filter_expenses_by_category(expenses, category):
    lambda expense: expense['category'] == category