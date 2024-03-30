class ExpenseTracker:
    def __init__(self):
        self.expenses = []


    def addExpense(self, amount, category, description):
        self.expenses.append({"amount": amount, "category": category, "description": description})


    def totalExpense(self):
        return sum(item["amount"] for item in self.expenses)



    def getExpensesByCategory(self, category):
        return [item for item in self.expenses if item["category"] == category]


def main():
    tracker = ExpenseTracker()


    while True:

#selection
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            tracker.addExpense(amount, category, description)
            print("Expense added successfully!")
        elif choice == "2":
            print("Total expenses:", tracker.totalExpense())
        elif choice == "3":
            category = input("Enter the category to view expenses: ")
            expenses = tracker.getExpensesByCategory(category)
            if expenses:
                print(f"Expenses for category '{category}':")
                for expense in expenses:
                    print(f"Amount: {expense['amount']}, Description: {expense['description']}")

            else:
                print("No expenses found for this category.")
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
