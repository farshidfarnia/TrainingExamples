username = input('Please enter username: ')
if len(username) < 3:
    print('username must be more than 3 characters!')
elif len(username) > 50:
    print('username must be at least 50 characters.')
else:
    print(f'username is: {username}\nPlease enter password: ')
