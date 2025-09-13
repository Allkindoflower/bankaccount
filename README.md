# Bank Account Simulator

A command-line Python application that simulates fundamental banking operations including user authentication, balance management, and transaction processing.

## 🔧 Features

- **Secure Authentication**: Username and PIN-based login system
- **Account Management**: Check account balance and transaction history
- **Deposit Operations**: Add funds with input validation
- **Withdrawal Operations**: Withdraw funds with balance verification
- **Multi-User Support**: Handle multiple user accounts with independent data
- **Input Validation**: Comprehensive error handling for invalid inputs
- **Clean Interface**: Clear screen functionality for enhanced user experience

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Terminal/Command Prompt access

### Installation

1. Fork and clone the repository:
   ```bash
   git clone <forked-repository-url>
   ```

2. Ensure all project files are in the same directory

3. Run the application:
   ```bash
   python "imports and running main logic.py"
   ```
   or run directly using your IDE.

## 💡 Usage

1. Launch the application using the command above
2. Enter your username and PIN when prompted
3. Select from the available menu options:
   - Check account balance
   - Make a deposit
   - Make a withdrawal
   - Exit the application

## 👥 Account Configuration

User accounts are defined in the `accounts` dictionary within the main script. To add new users:

```python
accounts = {
    'johnsmith': BankAccount('johnsmith', 1234, 1000.00),
    'janedoe': BankAccount('janedoe', 5678, 2500.00),
    # Add more accounts as needed
}
```

**Parameters:**
- `username`: User's login identifier
- `pin`: 4-digit authentication PIN
- `initial_balance`: Starting account balance

## 📁 Project Structure

```
bank-account-simulator/
├── imports and running main logic.py    # Main application file
├── README.md                           # Project documentation
├── accounts.py                         # Contains hardcoded mock accounts
├── actions.py                          # Bank account actions such as depositing
├── auth.py                             # User authenticaton logic
├── bankaccountclass.py                 # Contains the BankAccount object
├── utils.py                            # Helper functions

```

## 🔒 Security Features

- PIN-based authentication
- Input validation for all transactions
- Negative amount rejection for deposits and withdrawals
- Insufficient funds protection for withdrawals

## 🤝 Contributing

This project is designed for educational purposes. Feel free to fork, modify, and experiment with the code to enhance your understanding of Python programming concepts.

## 📄 License

This project is created for educational and learning purposes. No specific license is applied.

## 📞 Support

For questions or issues related to this educational project, please refer to the code comments and documentation within the source files.

---

## Important: This is a simulation program intended for learning Python programming concepts. It does not connect to real banking systems or handle actual financial transactions.
While this project is no longer maintained, the code includes comprehensive comments and documentation to help with understanding the implementation. You're encouraged to expand upon this foundation - consider turning it into a web application, adding a database backend, or implementing additional banking features as a learning exercise.
