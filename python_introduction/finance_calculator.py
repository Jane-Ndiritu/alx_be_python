monthly_income = int(input("What is your monthly income? "))
monthly_expenses = int(input("What are your monthly expenses? "))
savings = monthly_income - monthly_expenses
interest_rate = 0.05
annual_savings = savings * 12
interest_earned = annual_savings * interest_rate
print(f"Your annual savings are: {annual_savings}")