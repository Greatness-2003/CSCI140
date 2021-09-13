#retirement
savings = int(input('Enter total amount to save: '))  #target amount you wish to save
paycheck = int(input('Enter number of paychecks per year: '))   #paychecks received per year
first_months = savings//paycheck    #deduction per paycheck
last_month = first_months+(savings%paycheck)   #deduction for last month


print('You must make ' +str(paycheck-1)+  ' deductions of $' +str(first_months)+' and one final deduction of $' 
      +str(last_month)+ ' to save $' +str(savings)) 


#overduetax
PENALTY_RATE = 0.06 
EARTH_YEAR = 365 

tax = input('Enter amount of tax owed: ') #will be in format $100
rate = input('Enter interest rate: ') #will be in format 4%
late = int(input('Enter number of days overdue tax is: ')) #will be an integer

penalty = PENALTY_RATE * float(tax[1:])
interest = (float(rate[:-1])*(late/EARTH_YEAR)*float(tax[1:]))/100  #interest on tax
total = round(float(tax[1:]) + interest + penalty)   #total amount to pay

print('Your total payment is ' +str(total))


#marstoearth
earth_days= 365.25   #days in a year on Earth
mars_days = 687      #Earth-days in a year on Mars

mars_years = float(input('Enter number of Mars years: ')) #taking of input from user
mars_to_earth = int((mars_years * mars_days)//earth_days) #convert years on Mars to years on Earth

print('This is about', mars_to_earth, 'years on Earth.')


#convertage
D_PER_Y_PLANETS = [87.97, 687, 4331.87, 10760.27, 60189.55]   #earth days per year for various planets
PLANETS = ['Mercury', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

home_planet = int(input('Select your home planet: 1 for Mercury, 2 for Mars, 3 for Jupiter, ' 
                        '4 for Saturn, 5 for Neptune: '))     #prompts user for their home planet
age = float(input('Enter your age on your home planet: '))    #prompts for age on home planet
destination = int(input('Select a destination planet: 1 for Mercury, 2 for Mars, 3 for Jupiter, ' 
                        '4 for Saturn, 5 for Neptune: '))     #choose your destination

result = int((age * D_PER_Y_PLANETS[home_planet-1])/D_PER_Y_PLANETS[destination-1])  #converts age on age planet to age on destination planet
             
print('Your age on', PLANETS[destination-1], 'is about', result, 'years')
