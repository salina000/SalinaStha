class Test():
    a = 12
    b = 10

    def add(self):
        return self.a + self.b
    
    def multiply(self):
        return self.add()*2

data = Test()
print(data.add())
print(data.multiply())


class Car:
    color="blue"
obj=Car()
print(obj.color)


#constrictor

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

data = Person("Salina",18)
print(data.name)
print(data.age)



class Lamp:
    def __init__(self):
        self.is_on = False

obj = Lamp()
obj.is_on = True
print(obj.is_on)




class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balanced is {self.balance}")
        else:
            print("Deposit amount must be positive:")

    def withdraw(self, amount):
        if amount > self.balance:
           print("You don't have sufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance

account = BankAccount("")   
account.deposit(1000)
account.withdraw(800)
print(f"Final balance: {account.get_balance()}")





        


