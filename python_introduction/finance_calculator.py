# Define variables to receive the input

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Monthly saving operation

monthly_savings = monthly_income - monthly_expenses

# Project annual saving after one year operation


projected_savings = monthly_savings * 12 + int(monthly_savings * 12 * 0.05)

# Print results

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")