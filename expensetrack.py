class Expense:
    def __init__(self, amount, description, category):
        self.amount = amount
        self.description = description
        self.category = category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category):
        expense = Expense(amount, description, category)
        self.expenses.append(expense)

    def categorize_expenses(self):
        categories = {}
        for expense in self.expenses:
            if expense.category in categories:
                categories[expense.category].append(expense)
            else:
                categories[expense.category] = [expense]
        return categories

    def monthly_summary(self):
        total = sum(expense.amount for expense in self.expenses)
        return total

    def category_summary(self):
        categories = self.categorize_expenses()
        summary = {}
        for category, expenses in categories.items():
            total = sum(expense.amount for expense in expenses)
            summary[category] = total
        return summary

    def display_summary(self):
        print("Monthly Summary: ")
        print(f"Total Expenses: {self.monthly_summary()}")
        print("\nCategory-wise Summary: ")
        for category, total in self.category_summary().items():
            print(f"{category}: {total}")

    def run(self):
        while True:
            try:
                print("\nExpense Tracker Menu:")
                print("1. Add Expense")
                print("2. View Summary")
                print("3. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    amount = float(input("Enter the amount: "))
                    description = input("Enter the description: ")
                    category = input("Enter the category: ")
                    self.add_expense(amount, description, category)
                elif choice == 2:
                    self.display_summary()
                elif choice == 3:
                    print("Exiting the Expense Tracker. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter the correct data type.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
