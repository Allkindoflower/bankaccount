A simple command-line Python program that simulates basic bank account operations like login, balance check, deposit, and withdrawal.

Features
User login with username and PIN

Check account balance

Deposit money (rejects negative amounts)

Withdraw money (checks for sufficient funds and rejects negative amounts)

Supports multiple user accounts with independent balances

Clear screen command for better terminal experience

How to Run
Make sure you have Python 3 installed.

Clone or download this repository.

Run the program:
python bank_accountNEW.py
Follow on-screen prompts to login and perform account actions.

How to Add Accounts
Accounts are stored in the accounts dictionary in the script. To add a new user, add a new entry like:


accounts = {
    'johnsmith': BankAccount('johnsmith', 1234, 1000),
}

License
This project is for learning purposes and has no license.

Update: made the code more modular by splitting related functions to their own py files
