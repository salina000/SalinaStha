# 9.Write a function that takes the radius of a circle and returns the area of the circle using the formula 𝜋*r^2. Use only positional arguments.


def circle_area(r):
   
    return 22/7* r*r
a=int(input("enter a number: "))
print(circle_area(a))


# 2.Create a function that takes a base and an exponent (both integers) and returns the power (i.e., base raised to the exponent). Use only positional arguments.

def power(base,exponent):
    result = []
    for i in range(exponent):
        result *= base
    return result

def power(base,exponent):
    return base**exponent
a=int(input("enter a number: "))
print(power)


# 6.Create a function that takes a string and a character as positional arguments, and returns the number of times the character appears in the string.

# def arg_func(string,char):
#     count=0
#     for ch in string:
#         if ch==char:
#             count+=1
#     return count
# result= arg_func("banana","a ")
# print(result)

# def arg_func(string,characters):
#     freq={}
#     for ch in freq:
#         if ch in freq:
#             freq[ch] =+1
#         else:
#             freq[ch] =1
#     return freq.get(characters,0)
# a= arg_func("enter a word: ","n")
# print("result: ",a)


# 5.Define a function that takes a list and a number as positional arguments, and returns a new list where every element is multiplied by that number.



def multiply_list_element(lists,num):
   new_list=[]
   for element in lists:
      new_list.append(element*num)
      return new_list
a=multiply_list_element([2,4,6],3)
print(a)
