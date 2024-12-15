import sqlite3
from hashlib import sha256

class FinanceApp:
    def __init__(self):
        self.conn = sqlite3.connect("finance_app.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                type TEXT CHECK(type IN ('income', 'expense')),
                category TEXT,
                amount REAL,
                date TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                category TEXT,
                limit_amount REAL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        self.conn.commit()

    def register_user(self, username, password):
        try:
            hashed_password = sha256(password.encode()).hexdigest()
            self.conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                              (username, hashed_password))
            self.conn.commit()
            print("User registered successfully!")
        except sqlite3.IntegrityError:
            print("Username already exists. Please try another.")

    def login_user(self, username, password):
        hashed_password = sha256(password.encode()).hexdigest()
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", 
                       (username, hashed_password))
        user = cursor.fetchone()
        if user:
            print("Login successful!")
            return user[0]
        print("Invalid credentials.")
        return None

    def add_transaction(self, user_id, transaction_type, category, amount, date):
        self.conn.execute('''
            INSERT INTO transactions (user_id, type, category, amount, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, transaction_type, category, amount, date))
        self.conn.commit()

    def view_transactions(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT type, category, amount, date FROM transactions
            WHERE user_id = ? ORDER BY date
        ''', (user_id,))
        transactions = cursor.fetchall()
        return transactions

    def check_budget(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT b.category, b.limit_amount, 
                   COALESCE(SUM(t.amount), 0) AS total_spent
            FROM budgets b
            LEFT JOIN transactions t 
                ON b.user_id = t.user_id AND b.category = t.category AND t.type = 'expense'
            WHERE b.user_id = ?
            GROUP BY b.category
        ''', (user_id,))
        budgets = cursor.fetchall()
        return budgets

    def generate_report(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT type, SUM(amount) FROM transactions 
            WHERE user_id = ? GROUP BY type
        ''', (user_id,))
        report_data = {row[0]: row[1] for row in cursor.fetchall()}
        income = report_data.get('income', 0)
        expenses = report_data.get('expense', 0)
        savings = income - expenses
        return {'income': income, 'expenses': expenses, 'savings': savings}

    def set_budget(self, user_id, category, limit_amount):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO budgets (user_id, category, limit_amount)
            VALUES (?, ?, ?)
        ''', (user_id, category, limit_amount))
        self.conn.commit()
        print(f"Budget for {category} set to ${limit_amount:.2f}")
