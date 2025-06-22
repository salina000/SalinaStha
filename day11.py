# break and continue
a=[1,2,3,4,5,6]


for i in a:
    if i==3:
        break
    print(i)

for i in a:
    if i==3:
        continue
    print(i)

print("------------")
b=[1,2,3,"test",4.0,3.4,"testing world"]


final=[]
for i in b:
    if isinstance(i,int) or isinstance(i,float):
        final.append(i)
    print(final)





#nested for loop
for i in [1,2]:
    print(i)
    for j in [5,6]:
        print(j)



    
print("--------------------")
data=[10,50,3,5,6,7,8]
for i in [data]:
    print(i)

for i in data:


    for j in  range(1,11,1):
        print(f'{i} X {j}={i*j}')


print("--------------------")
data2=[10,20,3,4,5,6,10,4,4,5]
for i in [data2]:
    print(i)


for i in data2:
    for j in range(1,11,1):
        print(f'{i} X {j}={i*j}')
    print("\n")


a=[1,2,3,3,None,None,4,5,None]
final=[]
for i in a:
    if i is None:
        continue
    final.append(i)
    print(final)





# range=(50,100) even number

even_numbers=[num for num in range(50,101,2)]
print(even_numbers)

#i % 2 == 0 checks whether the range is even or odd
even_numbers = [i for i in range(50, 101) if i % 2 == 0]
print(even_numbers)

