# The table below outlines the grade boundaries on a certain university course. 
# Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

points = int(input("How many points [0-100]: "))

if points < 0 or points > 100:
    grade = "impossible!"
elif points >= 0 and points <= 49:
    grade = "fail"
elif points >= 50 and points <= 59:
    grade = "1"
elif points >= 60 and points <= 69:
    grade = "2"
elif points >= 70 and points <= 79:
    grade = "3"
elif points >= 80 and points <= 89:
    grade = "4"
elif points >= 90 and points <= 100:
    grade = "5"

print(f"Grade: {grade}")