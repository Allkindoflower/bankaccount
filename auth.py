#this file stores authentication functions
from accounts import accounts

def username_auth():
    max_username_attempt = 3
    current_username_attempt = 0
    print('Enter your username: ')
    while True:
        if current_username_attempt >= max_username_attempt:
            print('Too many wrong attempts! Try again later')
            break
            #lock attempts for some time logic here
        else:
            username_input = input('> ').strip().lower()
            if username_input in accounts:
                return username_input
            else:
                print('That username does not exist, try something else.')
                current_username_attempt += 1
def pin_auth(username_input):
    max_pin_attempt = 3
    current_pin_attempt = 0
    while True:
        try:
            pin_input = int(input('Enter your pin: '))
            if pin_input == accounts[username_input]._pin and accounts[username_input].status == 'unblocked':
                print('Login successfull!')
                return accounts[username_input]
            else:
                current_pin_attempt += 1
                print(f'Wrong PIN, (remaining attempts: {max_pin_attempt - current_pin_attempt})')      
                if current_pin_attempt >= max_pin_attempt:
                    accounts[username_input].status = 'blocked'
                    print('Your account has been blocked! Please contact your bank.')
                    return
        except ValueError:
            print('Please use numbers for your PIN.')

def login():
    username = username_auth()
    if username:
        account = pin_auth(username)
        return account
    else:
        print('Something went wrong, please try again.')
