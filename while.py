number = int(input("Please enter a number between -10 and 10: ")) # Asks the user to input a number between -10 and 10 and casts this as an integer
divider = 1 # Created a variable called diviider - after each loop the value of divider increments by one
total_number = 0
total_number += number # When a number is chosen this is added to the to variable total_number to keep track of the sum of the numbers added

while number != -1: # While loop this stops when the number inputted is equivalent to -1
    number = int(input("Please type in another number between -10 and 10: ")) # Prompts the user to put in another number
    divider = divider + 1 # Increments the value of divider for each run through each loop
    total_number += number # Adds the number inputted to the tota value of total number

average = total_number/divider # Calculates average of total number divided by the divider
print("The average of your numbers is: ", average) # Prints the average of your numbers is followed the average value