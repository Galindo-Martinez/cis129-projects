# This is my second Python lab in my CIS129 course
# This prints a simple receipt by asking the user what they bought

# User is asked a question
# Their input is turned into an integer
# Integer is then assigned to a variable
# This is done in one line of code
# Each of these contain \n making the input follow in a new line
print('\n***************************************')
print('Moca & Mac\'s Café')

coffees_bought = int(input('Number of coffees bought?\n'))
muffins_bought = int(input('Number of muffins bought?\n'))
teas_bought = int(input('Number of teas bought?\n'))
brownies_bought = int(input('Number of brownies bought?\n'))

print('***************************************')

# This is where I assigned all of the variables
# Starting off with the prices and tax
# The variables that follow are created using existing variables
# and arithmetic operators
coffee_price = 5
muffin_price = 4
tea_price = 4
brownie_price = 3

tax = .06

total_coffee_price = coffees_bought * coffee_price
total_muffin_price = muffins_bought * muffin_price
total_tea_price = teas_bought * tea_price
total_brownie_price = brownies_bought * brownie_price

# This line of code contains +\ making a too long of a line into two
total_without_tax = total_coffee_price + total_muffin_price +\
  total_tea_price + total_brownie_price
tax_for_purchase = total_without_tax * tax
total_with_tax = total_without_tax + tax_for_purchase

print('\n***************************************')
print('Moca & Mac\'s Café Receipt')

# This prints out consistent text along with user input from variables
# I also included if statements
# User input for 1 will give singular output in the items
# This part of the code also creates floats for the total prices
# The floats are formated with two decimal places
if coffees_bought == 1:
  print(coffees_bought, 'Coffee at $5 each: $', f"{total_coffee_price:.2f}")
else:
  print(coffees_bought, 'Coffees at $5 each: $', f"{total_coffee_price:.2f}")
if muffins_bought == 1:
  print(muffins_bought, 'Muffin at $4 each: $', f"{total_muffin_price:.2f}")
else:
  print(muffins_bought, 'Muffins at $4 each: $', f"{total_muffin_price:.2f}")
if teas_bought == 1:
  print(teas_bought, 'Tea at $4 each: $', f"{total_tea_price:.2f}")
else:
  print(teas_bought, 'Teas at $4 each: $', f"{total_tea_price:.2f}")
if brownies_bought == 1:
  print(brownies_bought, 'Brownie at $3 each: $', f"{total_brownie_price:.2f}")
else:
  print(brownies_bought, 'Brownies at $3 each: $', f"{total_brownie_price:.2f}")

# This prints out the tax amount with two decimal places
# The third line prints out the total with tax
# The variables are stored above and change depending on user input
print('6% tax: $', f"{tax_for_purchase:.2f}")
print('---------')
print('Total: $', total_with_tax)

print('***************************************')

# This is a message that thanks the user
print('\n¡Thank you for shopping at Moca & Mac\'s Café!')
print('¡Hope to see you again soon!')
