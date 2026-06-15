#  Expense Tracker

A simple yet feature-rich command-line Expense Tracker built in Python. It helps you manage your personal finances by tracking expenses, setting budgets, and generating summaries — all from an interactive menu.

---

##  Features

- **Set a Budget** — Define your total spending limit
- **Add Expenses** — Log expenses with amount, category, date, and description
- **View Expenses** — Display all recorded expenses with their index
- **Update Expenses** — Edit any field of an existing expense
- **Delete Expenses** — Remove an expense by its index
- **Search Expenses** — Filter expenses by category and/or date
- **Monthly Summary** — Get total spending for a specific month
- **Category-wise Summary** — See how much you've spent in a given category
- **Remaining Budget** — Check how much budget is left
- **Budget Status** — Get a quick status of whether you're on track or over budget

---

##  Getting Started

### Prerequisites

- Python 3.6 or higher

### Run the Program

```bash
python expense_tracker.py
```

No external libraries are required — the project uses only Python's standard library.

---

##  Usage

When you run the program, a welcome message is displayed and two demo expenses are pre-loaded. You are then presented with an interactive menu:

```
--- MENU ---
1.  Set Budget
2.  Add Expense
3.  View Expenses
4.  Calculate Total Expenses
5.  Update Expense
6.  Delete Expense
7.  Search Expenses
8.  Monthly Summary
9.  Category-wise Summary
10. Remaining Budget
11. Budget Status
12. Exit
```

Enter the number corresponding to your desired action and follow the prompts.

### Example Workflow

```
Set budget → 100000
Add expense → 5000, Food, 2026-06-01, Groceries
Add expense → 4000, Shopping, 2026-06-06, Clothes
View expenses → lists all recorded entries
Budget status → "Budget is on track. Remaining budget: 91000"
```

---

## Project Structure

```
expense_tracker.py   # Main file containing the ExpenseTracker class and menu
README.md            # Project documentation
```

---

## Class Overview

### `ExpenseTracker`

| Method | Description |
|---|---|
| `set_budget(budget)` | Sets the total budget |
| `add_expense(amount, category, date, description)` | Adds a new expense |
| `view_expenses()` | Prints all expenses with their index |
| `calculate_total_expenses()` | Returns the sum of all expense amounts |
| `update_expense(index, ...)` | Updates fields of an expense at the given index |
| `delete_expense(index)` | Deletes the expense at the given index |
| `search_expenses(category, date)` | Filters expenses by category and/or date |
| `monthly_summary(month)` | Returns total spending for a given month (`YYYY-MM`) |
| `category_wise_summary(category)` | Returns total spending for a given category |
| `remaining_budget()` | Returns `budget - total expenses` |
| `budget_status()` | Prints a human-readable budget status |
| `display_welcome_message()` | Prints a welcome message (decorated with a separator) |

---

##  Input Formats

| Field | Format | Example |
|---|---|---|
| Date | `YYYY-MM-DD` | `2026-06-15` |
| Month (for summary) | `YYYY-MM` | `2026-06` |
| Amount | Positive number | `1500` or `1500.50` |
| Category | Non-empty string | `Food`, `Travel` |

---

##  Input Validation

The tracker validates all inputs and prints descriptive error messages for:
- Negative or non-numeric amounts
- Empty category, date, or description strings
- Out-of-range expense indices
- Non-numeric menu selections

---
