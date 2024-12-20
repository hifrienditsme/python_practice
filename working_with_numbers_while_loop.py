# Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.
# After reading in the numbers the program should print out how many numbers were typed in.
# The program should also print out the sum and mean of all the numbers typed in.  
# You may assume the user will always type in at least one valid non-zero number.
# The program should also print out statistics on how many of the numbers were positive and how many were negative. 
# The zero at the end should not be included in any counts or calculations.


print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))
    sum += number

    if number < 0:
        negative += 1
    elif number > 0:
        positive += 1
    
    if number == 0:
        break

    count += 1
    mean = sum / count

print("Numbers typed in", count)
print("The sum of the numbers is ", sum)
print("The mean of the numbers is ", mean)
print("Positive numbers", positive)
print("Negative numbers ", negative)

