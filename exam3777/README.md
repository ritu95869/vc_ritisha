# Expense Tracker and Monthly Report

A beginner-friendly Python command-line application for a BCA practical.

## Features

- Add expenses with date, category, description, and amount
- View all expenses in a table
- Calculate total expenditure
- Find the highest expense
- Calculate category-wise spending
- Generate a monthly spending report
- Set a different budget for each month
- Check monthly spending, remaining budget, and budget warnings
- Validate dates, months, categories, descriptions, and amounts
- Uses only Python standard libraries

## Project structure

```text
exam3777/
├── expense_tracker.py
├── README.md
└── TEST_CASES.md
```

Expenses are stored in memory using a list of dictionaries. They are not saved after the program closes, which keeps the project simple and suitable for a practical demonstration.

## Requirements

- Python 3.8 or newer
- Visual Studio Code (recommended, but not required)
- No external packages

## Run in VS Code

1. Open the `exam3777` folder in Visual Studio Code.
2. Open `expense_tracker.py`.
3. Open **Terminal > New Terminal**.
4. Run:

```bash
python expense_tracker.py
```

If `python` does not work on your system, try:

```bash
python3 expense_tracker.py
```

## Date and month formats

- Expense date: `YYYY-MM-DD`, for example `2026-09-23`
- Budget/report month: `YYYY-MM`, for example `2026-09`

## Budget behavior

Set a budget for a month using **Set Monthly Budget**. Use **Check Budget** to see spending and remaining budget. A warning is displayed when spending reaches 80% or more of the budget. If spending is greater than the budget, the over-budget warning is shown instead.

## Example stored expense

```python
{
    "date": "2026-09-23",
    "category": "Food",
    "description": "Lunch",
    "amount": 250.0
}
```
