savings = int(input('Enter total amount to save: '))  #target amount you wish to save
paycheck = int(input('Enter number of paychecks per year: '))   #paychecks received per year
first_months = savings//paycheck    #deduction per paycheck
last_month = first_months+(savings%paycheck)   #deduction for last month


print('You must make ' +str(paycheck-1)+  ' deductions of $' +str(first_months)+' and one final deduction of $' 
      +str(last_month)+ ' to save $' +str(savings)) 
