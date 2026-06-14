class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = 0

    def set_budget(self, budget):
        if isinstance(budget, (int, float)) and budget >= 0:
            self.budget = budget
        else:
            print("Invalid budget. Please enter a non-negative number.")

    def add_expense(self, amount, category, date, description):
        if not isinstance(amount, (int, float)) or amount < 0:
            print("Invalid amount. Please enter a non-negative number.")
            return
        if not isinstance(category, str) or not category:
            print("Invalid category. Please enter a non-empty string.")
            return
        if not isinstance(date, str) or not date:
            print("Invalid date. Please enter a non-empty string.")
            return
        if not isinstance(description, str) or not description:
            print("Invalid description. Please enter a non-empty string.")
            return

        expense = {
            "amount": amount,
            "category": category,
            "date": date,
            "description": description
        }
        self.expenses.append(expense)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, expense in enumerate(self.expenses):
            # Index bhi print kar diya taaki update/delete karne me aasan ho
            print(f"Index: {i} | Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}, Description: {expense['description']}")

    def calculate_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def update_expense(self, index, amount=None, category=None, date=None, description=None):
        if index < 0 or index >= len(self.expenses):
            print("Invalid index. Please enter a valid expense index.")
            return
        if amount is not None:
            if isinstance(amount, (int, float)) and amount >= 0:
                self.expenses[index]['amount'] = amount
            else:
                print("Invalid amount. Please enter a non-negative number.")
        if category is not None:
            if isinstance(category, str) and category:
                self.expenses[index]['category'] = category
            else:
                print("Invalid category. Please enter a non-empty string.")
        if date is not None:
            if isinstance(date, str) and date:
                self.expenses[index]['date'] = date
            else:
                print("Invalid date. Please enter a non-empty string.")
        if description is not None:
            if isinstance(description, str) and description:
                self.expenses[index]['description'] = description
            else:
                print("Invalid description. Please enter a non-empty string.")

    def delete_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            print("Invalid index. Please enter a valid expense index.")
            return
        del self.expenses[index]

    def search_expenses(self, category=None, date=None):
        results = []
        for expense in self.expenses:
            if (category is None or expense['category'] == category) and (date is None or expense['date'] == date):
                results.append(expense)
        return results

    def monthly_summary(self, month):
        total = 0
        for expense in self.expenses:
            if expense['date'].startswith(month):
                total += expense['amount']
        return total

    def category_wise_summary(self, category):
        total = 0
        for expense in self.expenses:
            if expense['category'] == category:
                total += expense['amount']
        return total

    def remaining_budget(self):
        return self.budget - self.calculate_total_expenses()

    def budget_status(self):
        remaining = self.remaining_budget()
        if remaining > 0:
            print(f"Budget is on track. Remaining budget: {remaining}")
        elif remaining == 0:
            print("Budget is fully utilized.")
        else:
            print(f"Budget exceeded by {-remaining}. Consider reviewing your expenses.")

    # Ise staticmethod bana diya taaki decorater standard tarike se chal sake
    @staticmethod
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("============================================")
            result = func(*args, **kwargs)
            print("============================================")
            return result
        return wrapper

    @my_decorator
    def display_welcome_message(self):
        print("Welcome to the Expense Tracker!")


def menu(tracker):
    while True:
        print("\n--- MENU ---")
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Calculate Total Expenses")
        print("5. Update Expense")
        print("6. Delete Expense")
        print("7. Search Expenses")
        print("8. Monthly Summary")
        print("9. Category-wise Summary")
        print("10. Remaining Budget")
        print("11. Budget Status")
        print("12. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                budget = float(input("Enter your budget: "))
                tracker.set_budget(budget)
            except ValueError:
                print("Invalid input. Please enter a valid number for budget.")
        elif choice == 2:
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                date = input("Enter expense date (YYYY-MM-DD): ")
                description = input("Enter expense description: ")
                tracker.add_expense(amount, category, date, description)
            except ValueError:
                print("Invalid amount entry.")
        elif choice == 3:
            tracker.view_expenses()
        elif choice == 4:
            print(f"Total expenses: {tracker.calculate_total_expenses()}")
        elif choice == 5:
            try:
                index = int(input("Enter the index of the expense to update: "))
                amount = input("Enter new amount (leave blank to keep unchanged): ")
                category = input("Enter new category (leave blank to keep unchanged): ")
                date = input("Enter new date (leave blank to keep unchanged): ")
                description = input("Enter new description (leave blank to keep unchanged): ")
                
                # Blank input handle karne ke liye safe float conversion
                actual_amount = float(amount) if amount.strip() else None
                
                tracker.update_expense(
                    index,
                    actual_amount,
                    category if category.strip() else None,
                    date if date.strip() else None,
                    description if description.strip() else None,
                )
            except ValueError:
                print("Invalid index or amount input.")
        elif choice == 6:
            try:
                index = int(input("Enter the index of the expense to delete: "))
                tracker.delete_expense(index)
            except ValueError:
                print("Invalid index.")
        elif choice == 7:
            category = input("Enter category to search (leave blank to ignore): ")
            date = input("Enter date to search (leave blank to ignore): ")
            results = tracker.search_expenses(category if category.strip() else None, date if date.strip() else None)
            for expense in results:
                print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}, Description: {expense['description']}")
        elif choice == 8:
            month = input("Enter month to summarize (YYYY-MM): ")
            print(f"Total expenses for {month}: {tracker.monthly_summary(month)}")
        elif choice == 9:
            category = input("Enter category to summarize: ")
            print(f"Total expenses for category '{category}': {tracker.category_wise_summary(category)}")
        elif choice == 10:
            print(f"Remaining budget: {tracker.remaining_budget()}")
        elif choice == 11:
            tracker.budget_status()
        elif choice == 12:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 12.")


# --- Demo / test run ---
if __name__ == "__main__":
    E1 = ExpenseTracker()
    E1.display_welcome_message() # Ab decorator automatic chalega
    
    # Demo data add karna
    E1.set_budget(100000)
    E1.add_expense(5000, "Food", "2026-06-01", "Groceries")
    E1.add_expense(4000, "Shopping", "2026-06-06", "Clothes")
    
    # Menu start karna
    menu(E1)