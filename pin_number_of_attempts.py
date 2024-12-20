# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321 . 
# The program should then print out the number of times the user tried different codes.
# If the user gets it right on the first try, the program should print out something a bit different: 
# "Correct! It only took you one single attempt!"

attempts = 0

while True:
    code = input("PIN: ")
    attempts += 1

    if code == "4321":
        success = True
        break

    if code != "4321":
        print("Wrong ")

if success and attempts == 1:
     print("Correct! It only took you one single attempt!")
elif success:
    print(f"Correct! It took you {attempts} attempts")
    