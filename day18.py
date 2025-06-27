#inheritance
#single inheritance
#multiply inheritance
#multilevel inheritance

#Parent class
class A():
    a=10
    b=12

#child class
class B(A):
    a="testing"
    c="Hello world"
    d=15

obj= B()
print(obj.a)


class Math():
    def __init__(self):
        print("I am here from parent.")
        self.a = 5
        self.b = 3

    def sum(self):
        return self.a + self.b
    
class Number(Math):
     def __init__(self):
        print("I am here from child.")
        self.a = 5
        self.b = 3
        #Math._init_(self)
        super().__init__()
    #...

obj = Number()
# print(obj.sum)


#### Assignment 
# Create a parent class Product with attributes name and price.
# Create a child class DiscountedProduct that has discount_percent.
# Write a method to return the final price after discount.


class Product():
    def __init__(self,name,price):
        self.name = name
        self.price = price


class DiscountedProduct(Product):
    def __init__(self, name, price,discount_percent):
        super().__init__(name, price)
        self.discount_percent = discount_percent
        

    def get_final_price(self):
        discount_amount = (self.discount_percent/100)*self.price
        final_price = self.price - discount_amount
        return final_price

product = DiscountedProduct("bag",1000,10)
print(f"final price after discount is: {product.get_final_price()}")     

#### Assignment 
#  Create a class called `BankAccount` with a constructor that takes `account_holder` and `balance` (default 0).
#  Add methods:
#    - `deposit(amount)`: adds to balance
#    - `withdraw(amount)`: subtracts from balance if enough balance is available
#    - `get_balance()`: returns the current balance
#  Create an object and perform deposit and withdrawal operations.

class Account:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self,account_number,balance,interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
     
    def calculate_interest(self):
        return self.balance * self.interest_rate

Account = SavingsAccount("12345",100000,0.5)
print(Account.calculate_interest())

     

#### Assignment
# University ➝ Faculty ➝ Student
# Base class: University with attributes: university_name, location.
# Child class: Faculty with: faculty_name, dean.
# Grandchild class: Student with: student_name, roll_no, course.

# Write a method in Student to display full details of student with their faculty and university.

class University:
    def __init__(self,university_name,location):
        self.university_name = university_name
        self.location = location

class Faculty(University):
    def __init__(self,university_name,location,faculty_name,dean):
        super().__init__(university_name,location)
        self.faculty_name = faculty_name
        self.location = location
        self.dean = dean

class Student(Faculty):
    def __init__(self, university_name, location, faculty_name, dean, student_name, roll_no, course):
        super().__init__(university_name, location, faculty_name, dean)
        self.student_name = student_name
        self.roll_no = roll_no
        self.course = course

    def display_full_details(self):
        print(f"Student Name : {self.student_name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Course : {self.course}")
        print(f"Faculty : {self.faculty_name}")
        print(f"Dean : {self.dean}")
        print(f"University : {self.university_name}")
        print(f"Location : {self.location}")


student1 = Student(
    university_name= "Tribhuvan University",
    location = "Kathmandu",
    faculty_name="Engineering",
    dean="Mr. Sangam",
    student_name="Salina Shrestha",
    roll_no="801136",
    course="Computer Science"
    )
student1.display_full_details()

class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
class B(A):
    def __init__(self,a ,b,c,d):
        super().__init__(a,b)
        self.c =c
        self.d = d

class C (B,A):
    def __init__(self, a, b, c, d,e,f):
        super().__init__(a, b, c, d)
        self.e = e
        self.f = f

    def display_details(self):
        print(f"a: {self.a}")
        print(f"b: {self.b}")
        print(f"c: {self.c}")
        print(f"d: {self.d}")
        print(f"e: {self.e}")
        print(f"f: {self.f}")

D = C(
    a = "s",
    b = "a",
    c ="l",
    d ="i",
    e ="n",
    f ="a"
)
D.display_details()



class Car():
    def move(self):
        return "on wheels"
    
class Aeroplane():
    def move():
        return "on fly"
    
obj1 = Car()
obj2  = Aeroplane()
for i in[obj1,obj2 ]:
    print(i.move())