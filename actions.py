#stores action functions
from auth import login
from utils import show_help_commands, clear


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

def accept_login():
    account = login()
    if account:
        account_actions(account)
    else:
        print('Login failed or account blocked.')