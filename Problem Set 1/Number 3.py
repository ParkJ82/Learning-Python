total_cost = 1000000

annual_salary = float(input('Starting annual salary: '))
original_annual_salary = annual_salary
semi_annual_raise = .07
portion_down_payment = 0.25
r = 0.04


def total_savings(current_savings):
    month = 0
    annual_salary = original_annual_salary
    while month <= 36:
        month +=1
        current_savings = current_savings + annual_salary*portion_saved/12 + (current_savings)*r/12
        if month in range (6, 100000000000000, 6):
            annual_salary = annual_salary * (1+semi_annual_raise)  
    return current_savings

portion_saved = 1
steps = 0
current_savings = 0
current_savings = total_savings(current_savings)
if (total_cost*portion_down_payment > current_savings):
    print("It is not possible to pay the down payment in three years.")
else:
    low = 0
    high = 10000
    while abs(total_cost*portion_down_payment - current_savings) > 100:
        portion_saved = (low + high)/(2*10000)
        month = 0
        current_savings = 0
        current_savings = total_savings(current_savings)
        if (total_cost*portion_down_payment - current_savings) > 100:
            low = portion_saved*10000
        elif (total_cost*portion_down_payment - current_savings) < -100: 
            high = portion_saved*10000
        steps += 1
    print ("Best Savings Rate: " + str(portion_saved))
    print ("Steps in bisection search " + str(steps))