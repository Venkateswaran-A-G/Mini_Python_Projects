import pandas as pd
import numpy as np
import os

CSV_FILE = 'expenses.csv'

def load_expenses():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
    else:
        df = pd.DataFrame(columns=['id', 'date', 'category', 'amount', 'description'])
        df.to_csv(CSV_FILE, index=False)
    return df

def add_expense():
    df = load_expenses()
    new_id = df['id'].max() + 1 if not df.empty else 1
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value for amount.")
    description = input("Enter description: ")
    new_expense = pd.DataFrame([{
        'id': new_id,
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }])
    df = pd.concat([df, new_expense], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    print("✅ Expense added successfully.")

def view_expenses():
    df = load_expenses()
    if df.empty:
        print("No expenses recorded.")
    else:
        print("\nAll Expenses:\n")
        print(df.to_string(index=False))

def search_expense_by_id():
    df = load_expenses()
    if df.empty:
        print("No expenses recorded.")
        return
    try:
        search_id = int(input("Enter expense ID to search: "))
    except ValueError:
        print("Invalid input! ID should be a number.")
        return
    result = df[df['id'] == search_id]
    if result.empty:
        print("No expense found with the given ID.")
    else:
        print("\nSearch Result:\n")
        print(result.to_string(index=False))

def update_expense():
    df = load_expenses()
    if df.empty:
        print("No expenses recorded.")
        return
    try:
        update_id = int(input("Enter expense ID to update: "))
    except ValueError:
        print("Invalid input! ID should be a number.")
        return
    if update_id not in df['id'].values:
        print("No expense found with the given ID.")
        return
    idx = df.index[df['id'] == update_id][0]
    date = input(f"Enter new date ({df.at[idx, 'date']}): ") or df.at[idx, 'date']
    category = input(f"Enter new category ({df.at[idx, 'category']}): ") or df.at[idx, 'category']
    while True:
        amount_input = input(f"Enter new amount ({df.at[idx, 'amount']}): ") or df.at[idx, 'amount']
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Invalid input! Amount must be numeric.")
    description = input(f"Enter new description ({df.at[idx, 'description']}): ") or df.at[idx, 'description']
    df.loc[idx, ['date', 'category', 'amount', 'description']] = [date, category, amount, description]
    df.to_csv(CSV_FILE, index=False)
    print("✅ Expense updated successfully.")

def delete_expense():
    df = load_expenses()
    if df.empty:
        print("No expenses recorded.")
        return
    try:
        delete_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Invalid input! ID should be a number.")
        return
    if delete_id not in df['id'].values:
        print("No expense found with the given ID.")
        return
    df = df[df['id'] != delete_id]
    df.to_csv(CSV_FILE, index=False)
    print("✅ Expense deleted successfully.")

def show_summary():
    df = load_expenses()
    if df.empty:
        print("No expenses recorded.")
        return
    amounts = df['amount'].to_numpy()
    total = np.sum(amounts)
    avg = np.mean(amounts)
    maximum = np.max(amounts)
    minimum = np.min(amounts)
    by_category = df.groupby('category')['amount'].sum()
    print("\n--- Expense Summary ---")
    print(f"Total Expense: {total}")
    print(f"Average Expense: {avg:.2f}")
    print(f"Maximum Expense: {maximum}")
    print(f"Minimum Expense: {minimum}\n")
    print("Expense by Category:")
    print(by_category.to_string())
    print("------------------------")

def menu():
    while True:
        print("\n--- Expense Tracker CLI ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense by ID")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Show Summary")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            search_expense_by_id()
        elif choice == '4':
            update_expense()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            show_summary()
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
