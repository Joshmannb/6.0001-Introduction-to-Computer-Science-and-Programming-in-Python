'''Part B: Saving, with a raise
   Salary increases every 6 months'''

portion_saved = float(input('Please enter the portion of your salary saved for the down payment: '))
total_cost = float(input('Please enter the cost of your dream home: '))
annual_salary = float(input('Please enter your annual salary: '))
semi_annual_raise = float(input('Please enter your semi-annual salary raise percentage, as a decimal: '))
def house_hunting(portion_saved, total_cost, annual_salary, semi_annual_raise):
    month = 0
    portion_down_payment = 0.25 # 首付是房價的25%
    current_savings = 0. # 現有存款
    r = 0.04 / 12 # 月投資回報率
    down_payment = total_cost * portion_down_payment

    while down_payment > current_savings:
        month += 1
        if month % 6 == 1 and month > 6:
            annual_salary += annual_salary * semi_annual_raise
        current_savings = current_savings + (annual_salary / 12) * portion_saved + current_savings * r
    return month

# print(house_hunting(portion_saved, total_cost, annual_salary))
if __name__ == '__main__':
    print(house_hunting(portion_saved, total_cost, annual_salary, semi_annual_raise))