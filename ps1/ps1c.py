'''Part C: Finding the right amount to save away
   '''

# portion_saved = float(input('Please enter the portion of your salary saved for the down payment: '))
# total_cost = float(input('Please enter the cost of your dream home: '))
# semi_annual_raise = float(input('Please enter your semi-annual salary raise percentage, as a decimal: '))
annual_salary = float(input('Please enter your annual salary: '))
def house_hunting(annual_salary, total_cost=1e6, semi_annual_raise=0.07):
    upper_portion_saved = 10000
    lower_portion_saved = 0
    count = 0
    target_month = 36
    portion_down_payment = 0.25 # 首付是房價的25%
    current_savings = 0. # 現有存款
    r = 0.04 / 12 # 月投資回報率
    down_payment = total_cost * portion_down_payment
    # print(down_payment)

    while not down_payment - 100 < current_savings < down_payment + 100:
        month = 0
        current_savings = 0.
        start_salary = annual_salary
        middle_portion_saved = int((upper_portion_saved + lower_portion_saved) / 2)
        count += 1
        while month != target_month:
            month += 1
            if month % 6 == 1 and month > 6:
                start_salary += start_salary * semi_annual_raise
            current_savings = current_savings + ((start_salary / 12) * middle_portion_saved) / 10000 + current_savings * r
            # print(current_savings - 100 > down_payment)
            # print(start_salary)
            if current_savings > down_payment + 100:
                upper_portion_saved = middle_portion_saved
                # print(month)
                break
        if current_savings < down_payment - 100:
            print(month)
            lower_portion_saved = middle_portion_saved
        # print(upper_portion_saved, lower_portion_saved)

    return (middle_portion_saved) / 10000, count



# print(house_hunting(portion_saved, total_cost, annual_salary))
if __name__ == '__main__':
    print('''Best savings rate: {0:.4f}
             Steps in bisecion search: {1:}'''.format(
                 house_hunting(annual_salary)[0],
                 house_hunting(annual_salary)[1]))