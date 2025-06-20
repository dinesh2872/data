#  Expense Tracker (Python CLI)

A simple command-line-based personal expense tracker built using Python, Pandas, NumPy — with optional visualization using Matplotlib.

---

##  Features
- Read expenses from `expenses.csv`
- Show total amount spent
- Highest and lowest expense
- Category-wise summary: totals, counts, % spent
- Optional pie chart generation
- Add new expenses directly from CLI
- Filter expenses by date range
- Export summary to `summary_report.csv`

---

##  How to Run

1. Install dependencies:
```bash
pip install pandas numpy matplotlib
```

## to Run Programme

```bash
python expense_tracker.py
```
## outputs

###
-- Expense Tracker ---
1. View Summary        
2. Add New Expense     
3. Filter by Date Range
4. Generate Pie Chart  
5. Exit
Choose an option: 1    
Total Spending Overview
Total Amount Spent: ₹5400
Highest Expense: ₹5000 on 2025-06-12 (June Rent)
Lowest Expense: ₹50 on 2025-06-11 (Rickshaw fare)

 Category-wise Analysis
           Total Spent  Transactions  % of Total
Category
Food               150             1        2.78
Rent              5000             1       92.59
Transport           50             1        0.93
Utilities          200             1        3.70

Summary report exported to summary_report.csv

--- Expense Tracker ---
1. View Summary
2. Add New Expense
3. Filter by Date Range
4. Generate Pie Chart
5. Exit
Choose an option: 4
Pie chart saved as expenses_pie_chart.png

--- Expense Tracker ---
1. View Summary
2. Add New Expense
3. Filter by Date Range
4. Generate Pie Chart
5. Exit
Choose an option:

###


