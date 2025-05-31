#this file stores bank account class
from decimal import Decimal
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