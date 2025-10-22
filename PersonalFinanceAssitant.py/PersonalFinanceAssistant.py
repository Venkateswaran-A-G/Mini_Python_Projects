import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

file = "budget.csv"
budget = {}
income = {"Income":0}
index = 0

def load_csv():
    global index
    if os.path.exists(file):
        df = pd.read_csv(file)
        if not df.empty:
            index = df['Sl.no'].max()
    else:
        df = pd.DataFrame(columns =["Sl.no","date","type","amount","payment_mode","description","Month"])
        df.to_csv(file,index=False)
        index = 0
    return df

def save_budget():
    df = pd.DataFrame(list(budget.items()), columns=['Category', 'Budget'])
    df.to_csv("budget_goals.csv", index=False)
    print("✅ Budget goals saved successfully!")
    
def save_income():
    df = pd.DataFrame(list(income.items()), columns=['Type', 'Amount'])
    df.to_csv("Income.csv", index=False)
    print("✅ Income saved successfully!")
    
def set_goals():
    load_csv()
    try:
        income["Income"] = float(input("Enter  you total Income: "))
        save_income()
        budget["Food"]= float(input("Enter the budget for 'Food & Groceries' category: "))
        budget["Travel"]= float(input("Enter the budget for 'Travel' category: "))
        budget["Entertainment"]= float(input("Enter the budget for 'Entertainment' category: "))
        budget["Shopping"]=float(input("Enter the budget for 'Shopping' category: "))
        if sum(budget.values()) > income["Income"]:
            print("Your budget is greater than your total income!!!")
            print("Please set a proper budget according to your income.")
            budget.clear()
            set_goals()
        save_budget()
    except:
        print("⚠️ Please enter valid numbers only!")

def add_amount():
    global index
    df = load_csv()
    types = ["Income","income"]
    new_type = input("Enter your type(Income/Expense):")
    new_date =input("Enter the date(YYYY/MM/DD): ")
    new_amount = float(input("Enter the amount: "))
    new_payment_mode = input("Enter the payment mode: ")
    new_desc = input("Enter the description(Salary/Food/Travel/Entertainment/Shopping): ")
    new_month = input("Enter the Month: ")
    index = index+1
    if new_type in types:
        income["Income"] += new_amount
        save_income()
        print("✅ Income added successfully!")
    else:
        if new_desc in budget:
            budget[new_desc] -= new_amount
            budget_summary()
            save_budget()
            print("✅ Expense added successfully!")
        else:
            print(f"⚠️ '{new_desc}' is not a valid budget category.")
    new_row = pd.DataFrame([{"Sl.no":index,"date": new_date,"type":new_type,"amount":new_amount,"payment_mode":new_payment_mode,"description":new_desc,"Month":new_month}])
    df = pd.concat([df,new_row],ignore_index = True)
    df.to_csv(file,index=False)
    print("✅ Transaction recorded successfully!")

def view_amount():
    df = load_csv()
    if df.empty:
        print("No amounts recorded.")
        return

    choice = input("Do you want to display complete data (Y/N): ").upper()
    if choice == "Y":
        print(df.to_string(index=False))
    else:
        element = input("Enter the element you want to filter (type/description): ").lower()

        if element == "type":
            category = input("Enter the category (Income/Expense): ").capitalize()
            print(df[df["type"] == category].to_string(index=False))

        elif element == "description":
            category = input("Enter the category (Food/Travel/Entertainment/Shopping): ").capitalize()
            if category in ["Food", "Travel", "Entertainment", "Shopping"]:
                print(df[df["description"] == category].to_string(index=False))
            else:
                print("⚠️ Invalid category name.")
        else:
            print("⚠️ Invalid filter type.")
def budget_summary():
    df = load_csv()
    total_spent = income.get("Income", 0) - sum(budget.values())
    print(f"💰 Total Amount Spent: ₹{total_spent:.2f}")
    print("📊 Remaining Amount in every category:")

    for desc, amt in budget.items():
        print(f"{desc} : ₹{amt:.2f}")
        if amt < 0:
            print(f"⚠️ Warning!! You have exceeded your {desc} budget.")
def monthly_analytics():
    df = load_csv()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="Month", y="amount", hue="description")
    plt.title("Monthly Spending by Category")
    plt.xlabel("Month")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    while(1):
        print("___________Menu__________")
        print("1.Set Budget Goals")
        print("2.Add income/expense.")
        print("3.Veiw Expenses")
        print("4.Budget Summary")
        print("5.Monthly Analytics")
        print("6.Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            set_goals()
        elif ch == 2:
            add_amount()
        elif ch == 3:
            view_amount()
        elif ch == 4:
            budget_summary()
        elif ch==5:
            monthly_analytics()
        elif ch == 6:
            exit(0)
        else:
            print("Invalid Choice")
main()