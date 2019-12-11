import random


class Dice():
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
while True:
    user_input = input('Enter "R" for roll or enter "E" for exit: ')
    if user_input.upper() == "E" or user_input.upper() == "EXIT":
        break
    elif user_input.upper() == "R" or user_input.upper() == "ROLL":
        print(dice.roll())
    else:
        print("Sorry, I don't understand that!")

