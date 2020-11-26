import random

try: 
    min_value = int(input("Enter the minimum value of the dice\n"))
    max_value = int(input("Enter the maximum value of the dice\n"))
except:
    print("Input invalid program will revert to defaults")
    min_value = 1
    max_value = 6
again = True

while again:
    print(random.randint(min_value, max_value))
    another_roll = input("Want to roll again?\n")
    if another_roll == "yes" or another_roll == "y":
        continue
    else:
        break