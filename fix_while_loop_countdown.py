# This program should print out a countdown. The code is as follows:
# ___________________________________________________________
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number > 0:
#     break

# print("Now!")
# ___________________________________________________________

# This should print out:
# Countdown!
# 5
# 4
# 3
# 2
# 1
# Now!

# However, the program doesn't quite work. Please fix it.

number = 5
print("Countdown!")
while True:
    print(number)
    number = number - 1
    if number < 1:
        break

print("Now!")
