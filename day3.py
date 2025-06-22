#Comparison operator
a=2
b=2
print(a==b)

m=45
n=45
print(m!=n)
print(m>n)
print(m<n)
print(m>=n)
print(m<=n)

# logical operator
# and or not
print(a==b and a>=b)
print(4==1 and 2>=2)
print(1==1 or 2>=2)
print(not(1==1 or 2==2))

fname="Salina"
lname="Shrestha"
age=17

print("Hey its me" +str(fname) + str(lname) +","+" " +str(age))
print("hey its me", fname, lname, ",",age)
print("hey its me" + " " + fname + " "+ lname +"," " " +str(age))

#f string or string formatting
result= f'hey its me {fname} {lname}, {age}'
print(result)


a=10
result=isinstance(a,str)
result2=isinstance(a,int)
print(result)
print(result2)
b='true'
result3=isinstance(b,int)
print(result3)


