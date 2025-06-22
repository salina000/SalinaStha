# if condition

'''
Syntax
if (True or false condition):
'''

a=10
b=11
if (a==b):
    print("testing")

else:
    print("this is else condition")
    
if(a==b):
    print("a and b are equal.")
elif(a>=b):
    print("a is greater.")
elif(a<=b):
    print("b is lower.")
else:
    print("failed")


math=int(input("Enter a math marks: "))
chem=int(input("Enter a chem marks: "))
phy=int(input("Enter a phy marks: "))
nepali=int(input("Enter a nepali marks: "))
english=int(input("Enter a english marks: "))

total=math+chem+phy+nepali+english
per=total/5

if(per>=90):
    print("Grade A")

elif(per<90 and per>=80):
    print("Grade B")
elif(per<80 and per>=70):
    print("Grade C")
else:
    print("Failed")

a=int(input("Enter a number: "))
print(type(a))

