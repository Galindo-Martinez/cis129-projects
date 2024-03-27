
# Ana Galindo
# 03272024
# This program collects data from the user and calculates a total
# along with a total payout.

# This variable starts off the first while loop.
keep_going = 'y'

# Declaration of variables. And start of first while loop.
# Once both while loops run and user inputs 'y' to keep going,
# variables reset to their starting positions.
while keep_going == 'y':
  total_bottles = 0
  counter = 1
  today_bottles = 0
  total_payout = 0
  
  # This while loop will run while counter is less than or equal to seven.
  # The total_bottles and total_payout variables are calculated.
  # counter is added one for every loop.
  while counter <= 7:
    today_bottles = int(input(f'Enter number of bottles returned for day #{counter}: '))
    counter = counter + 1
    total_bottles = total_bottles + today_bottles
    total_payout = total_bottles * .10

  # This prints out total_bottles and total_payout.
  print(f'\nThe total number of bottles collected is {total_bottles}')
  print(f'The total paid out is ${total_payout:.2f}\n')

  # This asks the user for an input
  # and will keep looping to the first while, while the answer is 'y'.
  keep_going = input('Do you want to enter another week\'s worth of data?\n(Enter y or n): ')
  print()
