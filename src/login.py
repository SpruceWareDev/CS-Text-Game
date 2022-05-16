logins = [['Tom', '1234'], ['Bob', '123'], ['Dave', 'qwerty']]


def login(username, password):
    for details in logins:
        if username == details[0] and password == details[1]:
            return username
        else:
            return None


def create_account(username, password):
    logins.append([username, password])


def login_menu():
    print('Welcome to Spruce Adventure!')
    print('Please login or create an account.')
    print('1. Login')
    print('2. Create Account')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        print('Please enter your username and password')
        username = input('Username: ')
        password = input('Password: ')
        if login(username, password) is None:
            print('Login unsuccessful. Try again!')
            login_menu()
        else:
            print('Login successful! Welcome, ' + username + '!')
            return username
    elif choice == '2':
        print('Please enter a username and password')
        username = input('Username: ')
        password = input('Password: ')
        create_account(username, password)
        print('Account created!')
        return username
    elif choice == '3':
        print('Quitting!')
        quit()
