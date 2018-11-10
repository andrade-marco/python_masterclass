# Program to test rolling back database changes
import sqlite3
import pytz
import datetime

# SQL commands
ACCOUNTS_CREATE = 'CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)'
ACCOUNTS_ADD = 'INSERT INTO accounts VALUES(?, ?)'
ACCOUNTS_UPDATE = 'UPDATE accounts SET balance = ? WHERE (name = ?)'
HISTORY_CREATE = """CREATE TABLE IF NOT EXISTS history (time TIMESTAMP KEY NOT NULL, account TEXT NOT NULL,
                    amount INTEGER NOT NULL, PRIMARY KEY (time, account))"""
HISTORY_ADD = 'INSERT INTO history VALUES(?, ?, ?)'
HISTORY_VIEW = """CREATE VIEW IF NOT EXISTS localhistory AS
                  SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime')
                  AS localtime, history.account, history.amount FROM history
                  ORDER BY history.time"""

# Creating tables in database
db = sqlite3.connect('accounts.sqlite')
db.execute(ACCOUNTS_CREATE)
db.execute(HISTORY_CREATE)
db.execute(HISTORY_VIEW)

# Account class
class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name, opening_balance=0):
        # Initialize cursor for database manipulation
        cursor = db.execute('SELECT name, balance FROM accounts WHERE (name = ?)', (name,))
        row = cursor.fetchone()

        # If account alredy exists, just initialize class instance values
        # Otherwise, add new entry to database table
        if row:
            self.name, self._balance = row
            print('Retrieved record for {}.'.format(self.name))
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute(ACCOUNTS_ADD, (name, opening_balance))
            cursor.connection.commit()
            print('Account created for  {}.'.format(self.name), end='')

        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()

        try:
            db.execute(ACCOUNTS_UPDATE, (new_balance, self.name))
            db.execute(HISTORY_ADD, (deposit_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        else:
            db.commit()
            self._balance = new_balance

    def deposit(self, amount):
        if amount > 0:
            self._save_update(amount)
            print('{:.2f} deposited'.format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print('{:.2f} withdrawn'.format(amount / 100))
        else:
            print('The amount must be greater than zero and no more than your account balance')
        return self._balance / 100

    def show_balance(self):
        print('Balance on account {} is {:.2f}'.format(self.name, self._balance / 100))


if __name__ == '__main__':
    john = Account('John')
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account('Terry')
    graham = Account('Graham', 9000)
    eric = Account('Eric', 7000)
    db.close()
