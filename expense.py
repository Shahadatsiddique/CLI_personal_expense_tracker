class Expense:
    def __init__(self, amount, category, date, note=""):
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "note": self.note
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["amount"], data["category"], data["date"], data.get("note", ""))

    def __str__(self):
        return f"{self.date} | {self.category:10} | ₹{self.amount:>8.2f} | {self.note}"