import os


class BankAccount():
    def __init__(self, username, pin, balance):
        self.username = username
        self.pin = pin
        self.balance = balance


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    try:
        while True:
            print('Enter your username: ')
            username_input = input('> ')
            pin_input = int(input('Enter your PIN: '))
            if username_input in accounts and pin_input == accounts[username_input].pin :
                print('Login successfull!')
                account = accounts[username_input]
                return account
            else:
                print('Wrong credentials, try again!')
    except ValueError:
        print('Please enter letters for your username and numbers for your PIN')

        
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
        elif user_command == 'help':
            clear()
            help()
        elif user_command == 'clear':
            clear()
        else:
            print('Invalid input, try logging in.')

def account_actions(account):
    help()
    while True:
        print('1-Check Balance 2-Deposit 3-Withdraw 0-quit')
        try:
            account_input = int(input('> '))
            if account_input == 1:
                clear()
                check_balance(account)
            elif account_input == 2:
                clear()
                deposit(account)
            elif account_input == 3:
                clear()
                withdraw(account)
            elif account_input == 0:
                clear()
                print('Exiting...')
                return
            else:
                print('Invalid input, please try something else!')
        except ValueError:
            print('Your choice has to be a number!')


def check_balance(account):
    print(f'You have ${account.balance} to your name.')

def deposit(account):
    print('Enter the amount you want to deposit: ')
    try:
        deposit_amount = float(input('> '))
        if deposit_amount < 0:
            print('You cannot deposit a negative amount of money!')
        else:
            account.balance += deposit_amount
            print('Deposit successfull!')
            check_balance(account)
    except ValueError:
        print('Please enter a valid number!')

def withdraw(account):
    print('Enter the amount you want to withdraw: ')
    try:
        withdraw_amount = float(input('> '))
        if withdraw_amount > account.balance:
            print('You cannot withdraw an amount more than your balance!')
        elif withdraw_amount < 0:
            print('You cannot withdraw a negative amount of money!')
        else:
            account.balance -= withdraw_amount
            print('Withdraw successfull!')
            check_balance(account)
    except ValueError:
        print('Please enter a valid number!')


def help():
    print('''login - to log in an account
help - see a list of commands
exit or quit - to quit program
clear - to clear the terminal window
''')


accounts = {
    'johnsmith': BankAccount('johnsmith', 1234, 1000),
    'ugurbastug': BankAccount('ugurbastug', 4321, 0)
}
        

mainlogic()

