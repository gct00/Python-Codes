
class Account:


    def __init__(self,number, total):
        self.number = number
        self.total = total 
        

    def deposit(self, value):
        self.total += value


    def withdraw(self, value):
        self.total -= value
