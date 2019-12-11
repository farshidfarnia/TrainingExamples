print('\n*** Welcome To car games ***')
welcome_user = ""
started = False
while True:
    welcome_user = input("> ").lower()
    if welcome_user == "start":
        if started:
            print('car already is started!')
        else:
            started = True
            print('car is started, ready to go!')
    elif welcome_user == "stop":
        if not started:
            print('car already is stopped.')
        else:
            started = False
            print('car is stopped.')
    elif welcome_user == "help":
        print('start - to start the car.\nstop - to stop the car.\nquit - to exit.')
    elif welcome_user == "quit":
        break
    else:
        print("Sorry, I don't understand that!")