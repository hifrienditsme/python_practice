# Please write a program which asks the user for a year, and prints out the next leap year.
# If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year.

year = int(input("Year: "))
add_year = 0

while True:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        elif (year + 4) % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    if leap == True:
        break  
    else:
        leap = False
        year += 1
        add_year += 1       

if add_year > 0:
    print(f"The next leap year after {year - add_year} is {year}")
else:
    print(f"The next leap year after {year} is {year + 4}")


# The model solution is much simpler:

# start_year = int(input("Year: "))
# year = start_year + 1
# while True:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             break
#     elif year % 4 == 0:
#         break
 
#     year += 1
 
# print(f"The next leap year after {start_year} is {year}")
 