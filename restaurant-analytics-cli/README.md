# Python CLI Restaurant Ordering & Menu Summary Tool

A foundational Python CLI project combining a customer menu-ordering interface with an admin dish-summary script. Customer orders are stored in `orders.csv` (`Customer, Course, Item, Quantity, Unit_Price, Total`), and the admin view uses `pandas` and `matplotlib` to group orders by course and plot pie charts of the most-ordered items.

## Engineering & Troubleshooting Log

### 1. `IndexError` & Empty Rows Breaking Matplotlib Pie Charts
* **Root Cause:** Writing orders to `orders.csv` on Windows without `newline=""` inserted blank CRLF rows between every order, crashing the admin summary parser when iterating over rows.
* **Fix:** Enforced `open("orders.csv", mode="a", newline="")` across the customer ordering module and added empty-row filtering (`df.dropna()`) before grouping quantities.

### 2. Schema Mismatch During Multi-Module Compilation
* **Root Cause:** Combining the customer ordering menu with the admin login and summary script caused string-concatenation bugs instead of numeric addition when totaling dish quantities.
* **Fix:** Explicitly cast the `Quantity` and `Total` columns to `int`/`float` and standardized the course labels (`Starters`, `Main Course`, `Dessert`, `Beverages`) so `matplotlib.pyplot.pie()` rendered accurate percentages.
