# Please write a program which asks the user for three letters.
# The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.
# You may assume the letters will be either all uppercase or all lowercase.

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if letter1 > letter2 and letter1 < letter3 and letter2 < letter3:
    middle = letter1
if letter1 < letter2 and letter1 > letter3 and letter2 > letter3:
    middle = letter1

if letter1 < letter2 and letter1 < letter3 and letter2 < letter3:
    middle = letter2
if letter1 > letter2 and letter1 > letter3 and letter2 > letter3:
    middle = letter2

if letter1 < letter2 and letter1 < letter3 and letter2 > letter3:
    middle = letter3
if letter1 > letter2 and letter1 > letter3 and letter2 < letter3:
    middle = letter3


print(f"The letter in the middle is {middle}")



# the model solution is more concise.

# letter1 = input("1st letter: ")
# letter2 = input("2nd letter: ")
# letter3 = input("3rd letter: ")
 
# if letter1 > letter2 and letter1 > letter3:
#     if letter2 > letter3:
#         middle = letter2
#     else:
#         middle = letter3
# elif letter2 > letter3:
#     if letter3 > letter1:
#         middle = letter3
#     else:
#         middle = letter1
# else:
#     if letter2 > letter1:
#         middle = letter2
#     else:
#         middle = letter1
 
# print("The letter in the middle is " + middle)
