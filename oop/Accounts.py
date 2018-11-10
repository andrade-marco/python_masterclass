# Bank account example
import datetime
import pytz


class Account:
    # Simple account class with balance
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), balance))
        print('Account created for ' + self._name)

    # Static method - shared by all instances of the class
    # but not created for each instance
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print('The amount must be greater than zero and no more than your account balance')
        self.show_balance()

    def show_balance(self):
        print('Balance is {}'.format(self._balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount >= 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print('{:6} {} on {} (local time was {})'.format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account('Tim', 0)
    tim.deposit(1000)
    tim.withdraw(500)
    tim.show_transactions()

    tim = Account('Steph', 2000)
    tim.deposit(1000)
    tim.withdraw(500)
    tim.show_transactions()
