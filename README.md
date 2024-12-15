Personal Finance Management Application
Overview
The Personal Finance Management Application is a simple command-line and graphical user interface (GUI) application built using Python and Tkinter. It helps users track their personal finances by allowing them to:

Register and log in
Add income and expense transactions
View transactions by category and date
Set and check budgets
Generate financial reports
Features
User Registration & Authentication: Register with a unique username and password, and log in to access personal financial data.
Income and Expense Tracking: Add income and expense transactions, categorized by type.
Budgeting: Set monthly budgets for different categories and check if spending exceeds those limits.
Financial Reports: Generate monthly financial reports showing income, expenses, and savings.
SQLite Database: All data (users, transactions, budgets) is stored persistently in an SQLite database.
Requirements
Python 3.x (Python 3.7 or later recommended)
Tkinter (for GUI interface)
SQLite3 (for database management)
Dependencies
Tkinter (Python's built-in library)
SQLite3 (Python's built-in library)
Installation
Clone the repository:

Download or clone this repository to your local machine.
Install Python:

Ensure Python 3.x is installed on your system. You can download it from Python's official site.
Install Dependencies:

Tkinter and SQLite3 are built-in libraries in Python, so there is no need to install them separately.
Run the Application:

Navigate to the project directory and run the following command to start the application:
bash
Copy code
python main.py
Usage
User Registration and Login
Register: Click on the "Register" button and provide a unique username and password.
Login: After registration, log in with your credentials.
Adding Transactions
Add Income: Click on the "Add Income" button to input income transactions.
Add Expense: Click on the "Add Expense" button to input expense transactions.
Budgeting
Set Budget: Set a budget limit for a category (e.g., "Food", "Transport").
Check Budget: View the budget status to see if you are within your set limits.
Financial Reports
Generate Report: View a summary of your income, expenses, and savings over time.
Viewing Transactions
View Transactions: See all your income and expense transactions, categorized and sorted by date.
File Structure
plaintext
Copy code
personal_finance_app/
├── finance_app.py       # Core logic of the application (database, transactions, reports)
├── gui.py               # GUI interface using Tkinter
├── main.py              # Entry point for the application (launches the GUI)
├── finance_app.db       # SQLite database file (stores users, transactions, budgets)
└── README.md            # This file
Description of Files
finance_app.py:

Contains the core logic for user registration, login, transaction management, budgeting, and report generation.
Implements database interactions with SQLite.
gui.py:

Implements the graphical user interface using Tkinter.
Includes screens for registration, login, adding transactions, setting budgets, viewing transactions, and generating reports.
main.py:

The entry point for the application.
Initializes the Tkinter GUI and starts the application.
finance_app.db:

The SQLite database file where user data, transactions, and budgets are stored.
How to Use
Run the Application:

Start the application by running the following command:
bash
Copy code
python main.py
Register a New User:

Click the "Register" button and provide a username and password to create a new account.
Log in:

After registration, log in with your username and password.
Add Transactions:

After logging in, you can add income or expense transactions by selecting the respective option.
Set and Check Budget:

Set budgets for different categories, and check if you have exceeded your spending limit in any category.
Generate Financial Reports:

View a summary of income, expenses, and savings for your tracked transactions.
Example Use Case
Register with the username "john_doe" and password "password123".
Add an income of $5000 under the category "Salary".
Add an expense of $200 under "Food".
Set a budget of $300 for the "Food" category.
Check the budget status to see if the food expenses are within the budget.
Generate a report to see total income, expenses, and savings.
