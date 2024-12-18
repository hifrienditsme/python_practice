# Let's create a program along the lines of the example above.
# This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no".
# Then the program should print out "okay then" and finish.

print("hi")

while True:
    answer = input("Shall we continue? ")
    if answer == "no":
        break
    print("hi")

print("okay then")
