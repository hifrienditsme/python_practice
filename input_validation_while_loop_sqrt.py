# Please write a program which asks the user for integer numbers.
# If the number is below zero, the program should print out the message "Invalid number".
# If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
# In either case, the program should then ask for another number.
# If the user inputs the number zero, the program should stop asking for numbers and exit the loop.



from math import sqrt
# sqrt function will not work without this line in the beginning of the program

while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        break
    if number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))

print("Exiting...")
