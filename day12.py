# while loop
a=1
while(a<=10):
    print("This is loop")
    a=a+1

a=1
while(a<=10):
    print(a)
    a=a+1
    
a=1
num=2
while(a<=10):
    print(f'{num} X {a} = {num*a}')
    a=a+1
    


data=[10,50,3]
length= len(data)
print(length)
index= 0
while(index<length):
    i=1
    while(i<10):
        print(f'{data[index]} X {i}= {data[index]*i}')
        i=i+1
        print('\n')
        index += 1
