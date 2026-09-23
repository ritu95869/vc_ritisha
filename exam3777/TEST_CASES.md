# Boundary and Functional Test Cases

Run `python expense_tracker.py` and use the menu to test each case.

| Test | Input/action | Expected result |
|---|---|---|
| No expenses | Select View, Total, Highest, Category-wise, or Monthly Report before adding data | A clear no-expenses message is displayed; the program does not crash |
| One expense | Add `2026-09-23`, `Food`, `Lunch`, `250` | One dictionary is added and displayed correctly |
| Multiple expenses | Add expenses in different categories and months | Totals, highest expense, and reports use all matching records |
| Same date | Add two or more expenses with the same valid date | All records remain separate and are included in totals |
| Invalid date format | `23-09-2026` | Error message; date is requested again |
| Impossible date | `2026-02-30` | Error message; date is requested again |
| Leap-year boundary | `2024-02-29` | Accepted; `2025-02-29` is rejected |
| Negative amount | `-100` | Error message; amount is requested again |
| Zero amount | `0` | Error message; amount is requested again |
| Non-numeric amount | `abc` | Error message; amount is requested again |
| Empty description | Press Enter or enter spaces | Error message; description is requested again |
| Invalid category | `Travel` | Error message; category is requested again |
| Case-insensitive category | `food` or `FOOD` | Accepted and stored as `Food` |
| Invalid month | `September 2026` or `2026-13` | Error message; month is requested again |
| No data for month | Request a valid month with no expenses | `No expenses found` is displayed |
| Exact budget | Set budget `1000`, add spending `1000` | Remaining budget is `0.00`; 80% warning is displayed |
| Exactly 80% | Set budget `1000`, add spending `800` | 80% warning is displayed |
| Slightly above budget | Set budget `1000`, add spending `1000.01` | Over-budget warning is displayed |
| Below 80% | Set budget `1000`, add spending `799.99` | No budget warning is displayed |
| Invalid menu choice | Enter `0`, `10`, or text | Error message; menu is shown again |

## Logical checks performed

- Empty lists are checked before calculating a maximum.
- Only records whose date starts with the selected `YYYY-MM` are included in a monthly report.
- Monthly budgets are stored separately by month, so one month's budget does not affect another month.
- The over-budget condition is checked before the 80% condition, so an amount above the budget receives the most specific warning.
- Amounts are rounded to two decimal places when entered and displayed.
