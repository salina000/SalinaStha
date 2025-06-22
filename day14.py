def user_info(name="SS", role="Hello"):
    print("name is ",name)
    print("role is", role)

user_info(name="Salina", role="Student")
user_info()

def calculate_discount(price, discount=10):
    discounted_price=price-price*discount/100
    print("price is: ",price)
    print("discount is: ",discount)
    print(discounted_price)
calculate_discount(price=150,)
calculate_discount(price=250, discount=15)


data = {
    "name":"Suman Shrestha",
    "total":560,
    "count":6
}


def student(marks):
    name = marks.get('name')
    total = marks.get('total')
    count = marks.get('count')

    per = total/count
    return f'{name} percentage is {per}%'


print(student(marks = data))
# formula = total/count
# Suman Shrestha percentage is 70%

sum_dict = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50,
    "f": 60,
    "g": 70,
    "h": 80,
    "i": 90,
    "j": 100
}
value=sum_dict.values()
sum=0
for i in value:
    sum = sum + i
    print(i)

print("sum",sum)

