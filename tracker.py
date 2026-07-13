import json
import os

from expense import Expense


class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self, amount, category, date, note=""):
        expense = Expense(amount, category, date, note)
        self.expenses.append(expense)
        self.save_expenses()

    def delete_expense(self, index):
        try:
            removed = self.expenses.pop(index)
            self.save_expenses()
            return removed
        except IndexError:
            raise ValueError("Invalid expense index")

    def view_expenses(self):
        return self.expenses

    def get_total(self):
        return sum(e.amount for e in self.expenses)

    def get_total_by_category(self):
        totals = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return totals

    def save_expenses(self):
        with open(self.filename, "w") as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=2)

    def load_expenses(self):
        if not os.path.exists(self.filename):
            self.expenses = []
            return
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(d) for d in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self.expenses = []