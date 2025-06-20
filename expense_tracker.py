import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def load_data(filename="expense.csv"):
    if not os.path.exists(filename):
        print(f"{filename} not found.")
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    return pd.read_csv(filename)

def total_overview(df):
    print("\n Total Spending Overview")
    total = df["Amount"].sum()
    highest = df.loc[df["Amount"].idxmax()]
    lowest = df.loc[df["Amount"].idxmin()]
    print(f"Total Amount Spent: ₹{total}")
    print(f"Highest Expense: ₹{highest['Amount']} on {highest['Date']} ({highest['Description']})")
    print(f"Lowest Expense: ₹{lowest['Amount']} on {lowest['Date']} ({lowest['Description']})")

def category_analysis(df):
    print("\n Category-wise Analysis")
    cat_group = df.groupby("Category")["Amount"].agg(["sum", "count"])
    cat_group["percent"] = (cat_group["sum"] / df["Amount"].sum()) * 100
    cat_group = cat_group.rename(columns={"sum": "Total Spent", "count": "Transactions", "percent": "% of Total"})
    print(cat_group.round(2))

    # Export to CSV
    cat_group.to_csv("summary_report.csv")
    print("\n Summary report exported to summary_report.csv")

def generate_pie_chart(df):
    cat_sum = df.groupby("Category")["Amount"].sum()
    plt.figure(figsize=(8, 6))
    cat_sum.plot.pie(autopct='%1.1f%%')
    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("expenses_pie_chart.png")
    print("Pie chart saved as expenses_pie_chart.png")

def add_expense(filename="expenses.csv"):
    print("\n Add New Expense")
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = float(input("Amount: ₹"))
    description = input("Description: ")
    new_entry = pd.DataFrame([[date, category, amount, description]], columns=["Date", "Category", "Amount", "Description"])
    new_entry.to_csv(filename, mode='a', index=False, header=not os.path.exists(filename))
    print("Expense added successfully!")

def filter_by_date(df):
    print("\n Filter by Date Range")
    start = input("Start Date (YYYY-MM-DD): ")
    end = input("End Date (YYYY-MM-DD): ")
    filtered = df[(df["Date"] >= start) & (df["Date"] <= end)]
    if filtered.empty:
        print("No expenses in the given range.")
    else:
        print(filtered)
        total_overview(filtered)
        category_analysis(filtered)

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. View Summary")
        print("2. Add New Expense")
        print("3. Filter by Date Range")
        print("4. Generate Pie Chart")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        df = load_data()
        if df.empty and choice != "2":
            print("No expense data found. Please add some expenses first.")
            continue

        if choice == "1":
            total_overview(df)
            category_analysis(df)
        elif choice == "2":
            add_expense()
        elif choice == "3":
            filter_by_date(df)
        elif choice == "4":
            generate_pie_chart(df)
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
