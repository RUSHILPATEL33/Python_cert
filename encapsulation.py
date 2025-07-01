class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
acct = BankAccount(1000)
acct.deposit(500)
print(acct.get_balance())
        