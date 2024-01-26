# import previous class definition and random number generator
import random

class yourBank(object):
  '''A demonstration of a class'''

  # an attribute to keep track of total number of accounts
  numb_accounts=0

  def __init__(self,name,balance):
    '''Class initialiser'''
    print("Creating a class")
    self.name=name
    self.balance=balance
    yourBank.numb_accounts+=1

  # methods
  def deposit(self,amt):
    '''Adds an amount of money'''
    self.balance=self.balance+amt

  def withdraw(self,amt):
    '''Removes an amount of money'''
    self.balance=self.balance-amt

  def auto_deposit(self):
    '''Automatically deposits £1000'''
    self.deposit(1000)
    print(f"£1000 has been automatically deposited to {self.name}'s account.")

  def inquiry(self):
    '''Returns the current balance'''
    return self.balance
  


if __name__ == '__main__':
    # Create an banc account
    account = yourBank("St", 5000)
    account.auto_deposit()
    print(f"Balance for {account.name}: {account.inquiry()}")