total_cost = float(input('Cost of dream home: '))
portion_saved = float(input('Portion of salary to be saved: '))
annual_salary = float(input('Starting annual salary: '))

current_savings = 0
portion_down_payment = 0.25
r = 0.04
month = 0


while total_cost*portion_down_payment > current_savings:
    month +=1
    current_savings = current_savings + annual_salary*portion_saved/12 + (current_savings)*r/12
    
print('Number of Months: ' + str(month))