import tkinter as tk
from tkinter import messagebox
from finance_app import FinanceApp

class FinanceAppGUI:
    def __init__(self, root):
        self.app = FinanceApp()
        self.user_id = None
        self.root = root
        self.root.title("Personal Finance Manager")
        self.root.geometry("400x500")
        self.build_login_screen()

    def build_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Personal Finance Manager", font=("Helvetica", 16)).pack(pady=20)

        self.username_entry = tk.Entry(self.root, width=30)
        self.username_entry.pack(pady=10)
        self.username_entry.insert(0, "Username")

        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.pack(pady=10)
        self.password_entry.insert(0, "Password")

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Register", command=self.register).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_id = self.app.login_user(username, password)
        if user_id:
            self.user_id = user_id
            self.build_main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.app.register_user(username, password)
        messagebox.showinfo("Registration", "Registration successful! You can now log in.")

    def build_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Welcome to Personal Finance Manager", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.root, text="Add Income", command=self.add_income).pack(pady=5)
        tk.Button(self.root, text="Add Expense", command=self.add_expense).pack(pady=5)
        tk.Button(self.root, text="View Transactions", command=self.view_transactions).pack(pady=5)
        tk.Button(self.root, text="Generate Report", command=self.generate_report).pack(pady=5)
        tk.Button(self.root, text="Set Budget", command=self.set_budget).pack(pady=5)
        tk.Button(self.root, text="Check Budgets", command=self.check_budget).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=5)

    def add_income(self):
        self.transaction_form("income")

    def add_expense(self):
        self.transaction_form("expense")

    def transaction_form(self, transaction_type):
        transaction_window = tk.Toplevel(self.root)
        transaction_window.title(f"Add {transaction_type.capitalize()}")

        tk.Label(transaction_window, text=f"{transaction_type.capitalize()} Category").pack(pady=5)
        category_entry = tk.Entry(transaction_window, width=30)
        category_entry.pack(pady=5)

        tk.Label(transaction_window, text="Amount").pack(pady=5)
        amount_entry = tk.Entry(transaction_window, width=30)
        amount_entry.pack(pady=5)

        tk.Label(transaction_window, text="Date (YYYY-MM-DD)").pack(pady=5)
        date_entry = tk.Entry(transaction_window, width=30)
        date_entry.pack(pady=5)

        def save_transaction():
            category = category_entry.get()
            amount = float(amount_entry.get())
            date = date_entry.get()
            self.app.add_transaction(self.user_id, transaction_type, category, amount, date)
            messagebox.showinfo("Success", f"{transaction_type.capitalize()} added successfully!")
            transaction_window.destroy()

        tk.Button(transaction_window, text="Save", command=save_transaction).pack(pady=10)

    def view_transactions(self):
        transactions = self.app.view_transactions(self.user_id)
        transaction_window = tk.Toplevel(self.root)
        transaction_window.title("Transactions")

        tk.Label(transaction_window, text="Your Transactions", font=("Helvetica", 14)).pack(pady=10)
        if not transactions:
            tk.Label(transaction_window, text="No transactions found.").pack()
        else:
            for t in transactions:
                tk.Label(transaction_window, text=f"{t[3]} - {t[0].capitalize()} - {t[1]} - ${t[2]:.2f}").pack()

    def generate_report(self):
        report_window = tk.Toplevel(self.root)
        report_window.title("Financial Report")

        tk.Label(report_window, text="Financial Report", font=("Helvetica", 14)).pack(pady=10)
        report = self.app.generate_report(self.user_id)

        if not report:
            tk.Label(report_window, text="No transactions available for the report.").pack()
        else:
            tk.Label(report_window, text=f"Income: ${report['income']:.2f}, Expenses: ${report['expenses']:.2f}, Savings: ${report['savings']:.2f}").pack()

    def set_budget(self):
        budget_window = tk.Toplevel(self.root)
        budget_window.title("Set Budget")

        tk.Label(budget_window, text="Category").pack(pady=5)
        category_entry = tk.Entry(budget_window, width=30)
        category_entry.pack(pady=5)

        tk.Label(budget_window, text="Limit Amount").pack(pady=5)
        limit_entry = tk.Entry(budget_window, width=30)
        limit_entry.pack(pady=5)

        def save_budget():
            category = category_entry.get()
            limit = float(limit_entry.get())
            self.app.set_budget(self.user_id, category, limit)
            messagebox.showinfo("Success", f"Budget for {category} set successfully!")
            budget_window.destroy()

        tk.Button(budget_window, text="Save", command=save_budget).pack(pady=10)

    def check_budget(self):
        budget_window = tk.Toplevel(self.root)
        budget_window.title("Budget Status")
        tk.Label(budget_window, text="Budget Status", font=("Helvetica", 14)).pack(pady=10)

        budgets = self.app.check_budget(self.user_id)

        if not budgets:
            tk.Label(budget_window, text="No budgets set.").pack()
        else:
            for category, limit, spent in budgets:
                status = "OK" if spent <= limit else "Exceeded"
                tk.Label(budget_window, text=f"Category: {category}, Limit: ${limit:.2f}, Spent: ${spent:.2f} - {status}").pack()

    def logout(self):
        self.user_id = None
        self.build_login_screen()
