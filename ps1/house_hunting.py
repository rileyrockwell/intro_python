annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0

# annual return: 0.04
r = 0.04

"""
at the end of each month, your savings increase by the return on your investment, plus a percentage of your (monthly_salary) * (annual_salary / 12)
"""

monthly_salary = annual_salary / 12
total_months = 0

while current_savings < portion_down_payment * total_cost:
    current_savings += monthly_salary * portion_saved
    current_savings += current_savings * (r/12)
    total_months += 1

print("Number of months: " + str(total_months))