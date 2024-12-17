# This program calculates the end of year bonus a customer receives on their loyalty card. 
# If there are less than a hundred points on the card, the bonus is 10 %
# In any other case the bonus is 15 %
# The program should work like this:
# How many points are on your card? 55
# Your bonus is 10 %
# You now have 60.5 points

# But there is a problem with the program, so with some inputs it doesn't work quite right:
# How many points are on your card? 95
# Your bonus is 10 %
# Your bonus is 15 %
# You now have 120.175 points

# Please fix the program so that there is always either a 10 % or a 15 % bonus, but never both.
# points = int(input("How many points are on your card? "))
# if points < 100:
#     points *= 1.1
#     print("Your bonus is 10 %")

# if points >= 100:
#     points *= 1.15
#     print("Your bonus is 15 %")

# print("You now have", points, "points")


points = int(input("How many points are on your card? "))
if points < 100:
    bonus = points * 1.1
    print("Your bonus is 10 %")

if points >= 100:
    bonus = points * 1.15
    print("Your bonus is 15 %")

print("You now have", bonus, "points")

# The suggested solution (a *= b is the same thing as a = a * b):
#   points = int(input("How many points are on your card? "))
#    if points < 100:
#      factor = 1.1
#       print("Your bonus is 10 %")
    
#    if points >= 100:
#      factor = 1.15
#      print("Your bonus is 15 %")

#    points *= factor
#    print("You now have", points, "points")
