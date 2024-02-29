# This is my second Python lab in my CIS129 course
# This prints a simple receipt by asking the user what they bought
# Prices are displayed first
print('Prices \ncoffee: $5 \nmuffin: $4')

# The user is then asked a question
# Their input is then turned into an integer
# And the integer is assigned to a variable
# This is done in one line of code
coffees_bought = int(input('\nHow many cups of coffee would you like \
to purchase? '))
muffins_bought = int(input('How many muffins would you like to purchase? '))

# This is where I assigned all of the variables
# Starting off with the prices and tax
# The variables that follow are created using existing variables and arithmetic operators
coffee_price = 5
muffin_price = 4
tax = .06
total_coffee_price = coffees_bought * coffee_price
total_muffin_price = muffins_bought * muffin_price
total_without_tax = total_coffee_price + total_muffin_price
tax_for_purchase = total_without_tax * tax
total_with_tax = total_without_tax + tax_for_purchase

# This is the first part of the receipt
# This prints out consistent text and input from the user stored in variables
print('\n***************************************')
print('My Coffee and Muffin Shop')

print('Number of coffees bought?')
print(coffees_bought)

print('Number of muffins bought?')
print(muffins_bought)

print('***************************************')

# This is the second part of the receipt
# This prints out consistent text along with user input from variables
# I also included if statements
# User input for 1 will give singular output in the items
# This part of the code also creates floats for the total prices
# The floats are formated with two decimal places
print('\n***************************************')
print('My Coffee and Muffin Shop Receipt')

if coffees_bought == 1:
  print(coffees_bought, 'Coffee at $5 each: $', f"{total_coffee_price:.2f}")
else:
  print(coffees_bought, 'Coffees at $5 each: $', f"{total_coffee_price:.2f}")
  
if muffins_bought == 1:
  print(muffins_bought, 'Muffin at $4 each: $', f"{total_muffin_price:.2f}")
else:
  print(muffins_bought, 'Muffins at $4 each: $', f"{total_muffin_price:.2f}")

# This prints out the tax amount for the purchase
# The final line prints out the total with tax
# The variables are stored above and change depending on the user input
print('6% tax: $', tax_for_purchase)
print('---------')
print('Total: $', total_with_tax)

print('***************************************')
