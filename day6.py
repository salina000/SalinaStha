#datatype
#list

#example
a=[1,2,3,4,5,6,444,"testing"]
print(type(a))
#pos index=>start with 0
#neg index=>start with -1
print(a[0],a[3])
print(a[-1],a[-4])

print(len(a))

print(a[1:4])
print(a[:5])
print(a[3:])
print(a[:])

a.append(10)
a.append("hi")

n=input("Enter a word to add in list: ")
print(a)

#insert
a.insert(1,"Hello")



#extends
data1= [1,2,3,4,5]
data2= [6,7,8,9,10,11,12,13]
data1.extend(data2)
data2.extend(data1)
print("extends",data1)
print("extends",data2)

# a=[1,2,3,[1,2,3],[1,1,3,5,[32,2,4,5]]]

#concat
data1= [1,2,3,4,5]
data2= [6,7,7,8,9,10,11,12,13]
data3=data1+data2
print(data3)



#data remove
#del
del data2[2]
print(data2)

#remove
data2.remove(7)
print(data2)


#pop
data2.pop()
print(data2)


#clear
data2.clear()
print(data2)

data2= [6,7,7,8,9,10,11,12,13]
print(data2.count(7))

data2.reverse()
data2.sort(reverse=True)
print(data2)
