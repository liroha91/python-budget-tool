# python-budget-tool/models.py
# Includes classes Account, Bill, Debt, SavingsGoal, and Transaction

#--------------------------------------------------
# Account Class
#--------------------------------------------------
class Account:
  def __init__(self, name, account_type, last_four=None, balance=0):
    self.name = name
    self.account_type = account_type
    self.last_four = last_four
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

  def transfer(self, other_account, amount):
    self.withdraw(amount)
    other_account.deposit(amount)

#--------------------------------------------------
# Bill Class
#--------------------------------------------------
class Bill:
  def __init__(self, name, amount, due_day, category, account=None, is_recurring=True):
    self.name = name
    self.amount = amount
    self.due_day = due_day
    self.category = category
    self.account = account
    self.is_recurring = is_recurring
    self.is_paid = False

  def mark_paid(self):
    self.is_paid = True

  def mark_unpaid(self):
    self.is_paid = False

  def is_due_soon(self):
    pass

#--------------------------------------------------
# Debt Class
#--------------------------------------------------
class Debt:
  def __init__(self, name, starting_balance, current_balance, minimum_payment, due_day, interest_rate=0, category="Debt"):
    self.name = name
    self.starting_balance = starting_balance
    self.current_balance = current_balance
    self.minimum_payment = minimum_payment
    self.due_day = due_day
    self.interest_rate = interest_rate
    self.category = category

  def make_payment(self, amount):
    self.current_balance -= amount

  def add_charge(self, amount):
    self.current_balance += amount

  def remaining_balance(self):
    return self.current_balance

#--------------------------------------------------
# SavingsGoal Class
#--------------------------------------------------
class SavingsGoal:
  def __init__(self, name, goal_amount, current_amount=0, target_date=None, category="Savings"):
    self.name = name
    self.goal_amount = goal_amount
    self. current_amount = current_amount
    self.target_date = target_date
    self.category = category

  def add_contribution(self, amount):
    self.current_amount += amount

  def withdraw(self, amount):
    self.current_amount -= amount

  def progress_percent(self):
    if self.goal_amount == 0:
      return 0
    return (self.current_amount / self.goal_amount) * 100

  def remaining_amount(self):
    return self.goal_amount - self.current_amount

#--------------------------------------------------
# Transaction Class
#--------------------------------------------------
class Transaction:
  def __init__(self, date, description, amount, category, transaction_type, account=None):
    self.date = date
    self.description = description
    self.amount = amount
    self.category = category
    self.transaction_type = transaction_type
    self.account = account

  def is_income(self):
    return self.transaction_type == "income"

  def is_expense(self):
    return self.transaction_type in ["bill", "debt_payment", "savings", "spending"]

  def is_transfer(self):
    return self.transaction_type == "transfer"
