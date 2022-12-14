
from dataclasses import dataclass, field


@dataclass
class Expense:
    name:str
    value: float
    date: str
    def setValue(self, value):
        self.value = value


@dataclass
class Account:
    id : int
    name: str
    budget: float
    list_of_expenses: list = field(default_factory=list)
  

    def addMoneyToAccount(self, money):
        self.budget = self.budget + money     
    def addExpenseToAccount(self, expd):
        self.list_of_expenses.append(expd)
        self.budget = self.budget - expd.value