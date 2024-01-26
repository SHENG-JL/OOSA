import random

class yourBank(object):
    '''A demonstration of a class'''

    # An attribute to keep track of the total number of accounts
    numb_accounts = 0

    def __init__(self, name, balance):
        '''Class initialiser'''
        print(f"Creating a bank account for {name}")
        self.name = name
        self.balance = balance
        yourBank.numb_accounts += 1

    # Methods
    def deposit(self, amt):
        '''Adds an amount of money'''
        self.balance += amt

    def withdraw(self, amt):
        '''Removes an amount of money'''
        self.balance -= amt

    def inquiry(self):
        '''Returns the current balance'''
        return self.balance

class evilBank(yourBank):
    '''Class to represent a bank that occasionally lies'''

    def inquiry(self):
        '''Overload the inquiry method to lie 50% of the time'''
        if random.random() > 0.5:
            return self.balance * 1.2  # Overstate balance by 20%
        else:
            return self.balance

if __name__ == '__main__':
    # Create an evil bank account
    evil_account = evilBank("B", 3000)
    for _ in range(5):
        print(f"Balance for {evil_account.name} (potentially overstated): {evil_account.inquiry()}")