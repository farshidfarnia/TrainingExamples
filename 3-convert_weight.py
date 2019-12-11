user_weight = input('Enter your weight: ')
unit_of_weight = input('press "L" for convert to pounds(lbs) or press "K" for convert to kilograms(kg): ')
if unit_of_weight.lower() == "k":
    print(f"Your weight is {int(user_weight)* 0.453592} kilogram.")
elif unit_of_weight.lower() == "l":
    print(f"Your weight is {int(user_weight)* 2.20462} pounds.")
else:
    print('please enter your weight properly.')
