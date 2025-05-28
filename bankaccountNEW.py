import os
import time
from decimal import Decimal, InvalidOperation

class BankAccount:
    def __init__(self, username, _pin, _balance, status='unblocked'):
        self.username = username
        self._pin = _pin
        self._balance = Decimal(_balance)
        self.status = status

    def check_balance(self):
        print(f'You have ${self._balance:.2f} to your name.')

    def deposit(self):
        print('Enter the amount you want to deposit: ')
        try:
            deposit_amount = Decimal(input('> '))
            if deposit_amount < 0:
                print('You cannot deposit a negative amount of money!')
            elif deposit_amount == 0:
                print('You cannot deposit "0".')
            else:
                self._balance += deposit_amount
                print('Deposit successful!')
                self.check_balance()
        except (ValueError, InvalidOperation):
            print('Please enter a valid number!')

        
    def withdraw(self):
        print('Enter the amount you want to withdraw: ')
        try:
            withdraw_amount = Decimal(input('> '))
            if withdraw_amount > self._balance:
                print('You cannot withdraw an amount more than your balance!')
            elif withdraw_amount < 0:
                print('You cannot withdraw a negative amount of money!')
            elif withdraw_amount == 0:
                print('You cannot withdraw "0".')
            else:
                self._balance -= withdraw_amount
                print('Withdraw successful!')
                self.check_balance()
        except (ValueError, InvalidOperation):
            print('Please enter a valid number!')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def accept_login():
    account = login()
    if account:
        account_actions(account)
    else:
        print('Login failed or account blocked.')

def mainlogic():
    print('Welcome to your bank account manager. Type "login" to log in your account.')
    while True:
        user_command = input('> ').strip().lower()
        if user_command == 'login':
            accept_login()
        elif user_command == 'exit' or user_command == 'quit':
            clear()
            time.sleep(2)
            print('Signing off...')
            quit()
        elif user_command == 'help':
            clear()
            show_help_commands()
        elif user_command == 'clear':
            clear()
        else:
            print('Invalid input, try logging in.')


def account_actions(account):
    show_help_commands()
    account.check_balance()
    while True:
        print('1-Check balance 2-Deposit 3-Withdraw 0-quit')
        try:
            account_input = int(input('> '))
            if account_input == 1:
                clear()
                account.check_balance()
            elif account_input == 2:
                clear()
                account.deposit()
            elif account_input == 3:
                clear()
                account.withdraw()
            elif account_input == 0:
                clear()
                print('Exiting...')
                print('Welcome to your bank account manager. Type "login" to log in your account.')
                return
            else:
                print('Invalid input, please try something else!')
        except ValueError:
            print('Your choice has to be a number!')



def show_help_commands():
    print('''login - to log in an account
help - see a list of commands
exit or quit - to quit program
clear - to clear the terminal window
''')


accounts = {
    'johnsmith': BankAccount('johnsmith', 1234, 1000),
    'ugurbastug': BankAccount('ugurbastug', 4321, 0),
    'namesurname': BankAccount('namesurname', 1111, 10000)
}
        

mainlogic()