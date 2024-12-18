# If the total value of gifts you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.
# When the gift is received from a close relative or a family member, the amount of tax to be paid is determined by a table (below).
# So, for a gift of 6000 euros the recipient pays a tax of 180 euros (100 + (6000 - 5000) * 0.08).
# Similarly, for a gift of 75000 euros the recipient pays a tax of 7100 euros (4700 + (75000 - 55000) * 0.12).
# Please write a program which calculates the correct amount of tax for a gift from a close relative. 

# Value of gift    ...	Tax at the lower limit ...	Tax rate for the exceeding part (%)
# 5000 — 25000     ...	100                    ...	8
# 25000 — 55000    ...	1700                   ...  10
# 55000 — 200000   ...  4700                   ...	12
# 200000 — 1000000 ...	22100                  ...	15
# 1000000 +        ...	142100                 ...	17

gift_value = float(input("Value of gift: "))

if gift_value < 1000000:
    if gift_value < 200000:
        if gift_value < 55000:
            if gift_value < 25000:
                if gift_value < 5000:
                    print("No tax!")
                else:
                    tax = (100 + (gift_value - 5000) * 0.08)
            else: 
                tax = (1700 + (gift_value - 25000) * 0.1)
        else:
            tax = (4700 + (gift_value - 55000) * 0.12)
    else:
        tax = (22100 + (gift_value - 200000) * 0.15)
else:
    tax = (142100 + (gift_value - 1000000) * 0.17)
   
    
if gift_value >= 5000:
    print(f"Amount of tax: {tax} euros")
