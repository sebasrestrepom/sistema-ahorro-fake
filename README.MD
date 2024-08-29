# Savings System - Python Project

## Description

This project implements a savings system in Python using a three-tier architecture: **Controllers**, **Services**, and **Repositories**. The application allows users to be registered, accounts to be associated with those users, and transactions (deposits and withdrawals) to be performed on those accounts. Fundamental Object-Oriented Programming (OOP) concepts such as encapsulation, inheritance, polymorphism, and abstraction are applied throughout the project.

## Object-Oriented Programming Concepts Applied

1. **Encapsulation**:
   - Classes such as `User`, `Account`, and `Transaction` encapsulate their data and methods, protecting internal attributes from unauthorized access and exposing only what's necessary through methods.

2. **Inheritance**:
   - The `User` class inherits from `Person`, reusing common attributes and methods while adding specific functionality, such as the ability to associate accounts.

3. **Polymorphism**:
   - The `Deposit` and `Withdrawal` subclasses of the `Transaction` class implement the `execute` method differently, allowing the same method to perform different actions depending on the subclass.

4. **Abstraction**:
   - Repositories and controllers provide a simplified interface to interact with the system, hiding the complexity of internal implementation.

## Requirements

- Python 3.6 or higher

## Installation and Execution Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/savings-system.git
   cd savings-system
Run the application:

Simply execute the main.py file to start the application:
```
python3 main.py
```

## Interacting with the System:

The system will prompt you to input data via the console to register users, create accounts, and perform transactions. Follow the on-screen instructions to operate the system.
### Example Usage

```
Starting the savings system...
Enter user identification: 123456789
Enter user names: John Doe
Enter user age: 30
User ID: 123456789, Name: John Doe, Age: 30 registered successfully.
Enter the account ID: 001
Enter the account type (e.g., Savings, Checking): Savings
Enter the account opening date (e.g., 2024-08-27): 2024-08-27
Account 001 created and associated with user John Doe.
Enter the transaction ID: T001
Enter the transaction type (Deposit/Withdrawal): Deposit
Enter the transaction amount: 1000
Deposit of 1000 completed successfully.
```

## Contributions

Contributions are welcome. If you'd like to contribute, please open an issue or a pull request on the GitHub repository.