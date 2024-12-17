# # Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in
# # degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out
# # "Brr! It's cold in here!".

# # Two examples of expected behavior:
# Please type in a temperature (F): 101 
# 101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

# Please type in a temperature (F): 21 
# 21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius Brr! It's cold in here!

temp = float(input("Please type in a temperature (F): "))
celsius = (temp - 32)  /  1.8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

if celsius < 0:
    print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius Brr! It's cold in here!")
else:
    print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")
    