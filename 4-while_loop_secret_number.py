counter = 0
while counter <= 5:
    print('*' * counter)
    counter += 1
print('Welcome')

secret_number = 16
user_guess = int(input('Enter a number between 0 to 20: '))

while user_guess != secret_number:
    if user_guess < secret_number:
        user_guess = int(input('Increase your number > '))
    elif user_guess > secret_number:
        user_guess = int(input('Decrease your number < '))
    else:
        user_guess == secret_number
print('*** Congratulations, you won! ***')