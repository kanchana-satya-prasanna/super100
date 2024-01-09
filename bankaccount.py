class BankAccount:
    def _init_(self, account_holder_name,account_number,balance):
          self.account_holder_name = account_holder_name
          self.account_number = account_number
          self.balance = balance


    def deposit(self,amount):
         self.balance += amount


    def withdraw(self,amount):
          if amount > self.balance:
             print("Insufficient funds")
          else:
             self.balance -= amount

    def display(self,balance):
          print("Available balance:",self.balance)