#helper functions
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help_commands():
    print('''login - to log in an account
help - see a list of commands
exit or quit - to quit program
clear - to clear the terminal window
''')
    
