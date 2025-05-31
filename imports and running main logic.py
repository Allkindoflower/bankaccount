#imports and running main logic here
import time
from bankaccountclass import BankAccount
from actions import account_actions, accept_login
from auth import login, username_auth
from utils import clear, show_help_commands
from accounts import accounts



def mainlogic():
    print('Welcome to your bank account manager. Type "login" to log in your account.')
    while True:
        user_command = input('> ').strip().lower()
        if user_command == 'login':
            accept_login()
        elif user_command == 'exit' or user_command == 'quit':
            clear()         
            print('Signing off...')
            time.sleep(2)
            quit()
        elif user_command == 'help':
            clear()
            show_help_commands()
        elif user_command == 'clear':
            clear()
        else:
            print('Invalid input, try logging in.')





if __name__ == '__main__':
    mainlogic()








