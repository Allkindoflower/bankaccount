import os


class BankAccount():
    def __init__(self, username, _pin, _balance):
        self.username = username
        self._pin = _pin
        self._balance = _balance
    def check_balance(self):
        print(f'You have ${self._balance} to your name.')


    def deposit(self):
        print('Enter the amount you want to deposit: ')
        try:
            deposit_amount = float(input('> '))
            if deposit_amount < 0:
                print('You cannot deposit a negative amount of money!')
            else:
                self._balance += deposit_amount
                print('Deposit successfull!')
                self.check_balance()
        except ValueError:
            print('Please enter a valid number!')


    def withdraw(self):
        print('Enter the amount you want to withdraw: ')
        try:
            withdraw_amount = float(input('> '))
            if withdraw_amount > self._balance:
                print('You cannot withdraw an amount more than your balance!')
            elif withdraw_amount < 0:
                print('You cannot withdraw a negative amount of money!')
            else:
                self._balance -= withdraw_amount
                print('Withdraw successfull!')
                self.check_balance()
        except ValueError:
            print('Please enter a valid number!')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def login():
        try:
            while True:
                print('Enter your username: ')
                username_input = input('> ')
                _pin_input = int(input('Enter your _pin: '))
                if username_input in accounts and _pin_input == accounts[username_input]._pin :
                    print('Login successfull!')
                    account = accounts[username_input]
                    return account
                else:
                    print('Wrong credentials, try again!')
        except ValueError:
            print('Please enter letters for your username and numbers for your _pin')
        
def mainlogic():
    print('Welcome to your bank account manager. Type "login" to log in your account.')
    while True:
        user_command = input('> ').strip().lower()
        if user_command == 'login':
            clear()
            account = login()
            if account:
                account_actions(account)
        elif user_command == 'exit' or user_command == 'quit':
            clear()
            quit()
        elif user_command == 'show_help_commands':
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
        print('1-Check _balance 2-Deposit 3-Withdraw 0-quit')
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