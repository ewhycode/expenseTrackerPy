class ExpenseTracker:
    def __init__(self):
        self.expense_records = []

    def addExpense(self, date, category, amount):
        self.expense_records.append({"date": date, "category": category, "amount": amount})

    def viewExpenses(self):
        if not self.expense_records:
            print("No expenses recorded yet.")
        else:
            print("Expense Records:")
            for record in self.expense_records:
                print(f"Date: {record['date']}, Category: {record['category']}, Amount: {record['amount']}")
