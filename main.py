from tracker import ExpenseTracker

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    tracker = ExpenseTracker()

    menu = """
1. Add expense
2. View all expenses
3. View total spending
4. View spending by category
5. Delete an expense
6. Exit
"""

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            amount = get_float_input("Amount: ")
            category = input("Category: ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            note = input("Note (optional): ").strip()
            tracker.add_expense(amount, category, date, note)
            print("Expense added.")

        elif choice == "2":
            expenses = tracker.view_expenses()
            if not expenses:
                print("No expenses yet.")
            for i, e in enumerate(expenses):
                print(f"{i}: {e}")

        elif choice == "3":
            print(f"Total spending: ₹{tracker.get_total():.2f}")

        elif choice == "4":
            totals = tracker.get_total_by_category()
            for cat, total in totals.items():
                print(f"{cat:10}: ₹{total:.2f}")

        elif choice == "5":
            index = int(get_float_input("Index to delete: "))
            try:
                removed = tracker.delete_expense(index)
                print(f"Deleted: {removed}")
            except ValueError as e:
                print(e)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()