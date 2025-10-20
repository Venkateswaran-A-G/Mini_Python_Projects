import pandas as pd
import numpy as np
import os

file = "budget.csv"
budget = {}
income = {}
index = 0

def load_csv():
    if os.path.exists(file):
        df = pd.read_csv(file)
    else:
        df = pd.DataFrame(columns =["Sl.no","date","type","amount","payment_mode","description","Month"])
        df.to_csv(file,index=False)
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