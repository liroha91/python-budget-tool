# python-budget-tool/budget.py
# Includes class Budget

#--------------------------------------------------
# Budget Class
#--------------------------------------------------
class Budget:
  def __init__(self):
    self.transactions = []
    self.bills = []
    self.debts = []
    self.savings_goals = []
    self.account = []

  def add_transaction(self, transaction):
    self.transactions.append(transaction)

  def add_bill(self, bill):
    self.bills.append(bill)

  def add_debt(self, debt):
    self.debts.append(debt)

  def add_savings_goal(self, savings_goal):
    self.savings_goals.append(savings_goal)

  def add_account(self, account):
    self.accounts.append(account)

  def total_income(self):
    return sum(t.amount for t in self.transactions if t.is_income())

  def total_expenses(self):
    return sum(t.amount for t in self.transactions if t.is_expense())

  def total_bills(self):
    return sum(bill.amount for bill in self.bills)

  def total_debt_payments(self):
    return sum(debt.minimum_payment for debt in self.debts)

  def total_savings_goals(self):
    return sum(goal.current_amount for goal in self.savings_goals)

  def leftover(self):
    return self.total_income() - self.total_expense()

  def category_totals():
    pass
