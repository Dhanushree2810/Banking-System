class Account:
    def __init__(self,name,account_no,balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient Balance"
        
class SavingsAccount(Account):
    def withdraw(self,amount):
        if self.balance - amount >= 1000:
            return super().withdraw(amount)
        else:
            return "Maintain Minimum Balance"