#function


def test_func():
    print("I am function")
    return 1,2 

print(test_func())
test_func


def my_func():
    print("Hello,What's up")
    return 1,2,3 
print(my_func())



# positional arg

def arg_func(a,b,c):
    print(a,b,c)
arg_func(3,2,1)


def user_info(name, role):
    print("name is ",name)
    print("role is", role)


name = input("enter your name ")
role = input("enter a role ")
user_info(name, role)




def shop_cart(price,quantity):
    return price*quantity
   
total= shop_cart(250,3)
print("total is", total)

#2: Define a function that accepts four parameters: length, width, height, and unit_price. It should calculate the cost to fill a box (volume × unit_price) using positional arguments only. Then call the function with appropriate values.

def para_func(length, width, height,unit_price):
    vol= length*width*height
    cost=vol*unit_price
    return cost

total_cost= para_func(2,3,4,5)
print("total cost: ",total_cost)



#1: Create a function that takes three integers and returns the second largest number among them. All three integers should be passed as positional arguments.

def second_largest(a,b,c):
    return (a,b,c)

result= second_largest(4,5,6)
print("second largest: ",result)







# 3: Write a function that takes two lists as positional arguments and returns a list containing the common elements between them. Do not use any keyword arguments or unpacking.

'''
def data_list(a,b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    return list(set(result))
'''

    