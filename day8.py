# dict

userinfo={
    "name":"Salina Shrestha",
    "age":18,
    "address":"Chunikhel",
    "test":[1,2,3]
}
print(type(userinfo))

print(userinfo["name"])
print(userinfo["address"])
print(userinfo["age"])
print(userinfo["test"])

userinfo['age']=17
print(userinfo)
userinfo['ages']="update key"
print(userinfo)

userinfo2={
    "role":"student",
    "age":18
}
userinfo.update(userinfo2)
print(userinfo)
print(len(userinfo))

print(userinfo2.get("ss"))
print(userinfo2.get("hi", "key doesnot exist"))
print(userinfo2.get("age", "key doesnot exist"))


#removing method from dict
test={
    "name":"broadway",
    "greet":"hello",
    "age":34
    
}
#del test["greet"]
test.pop("name")
test.popitem()
print(test)




user = {
    "name":"Sudan",
    "phone":[98062, 98449]
}




a = user.get("phone")
print(a)

print("number is ", a[0])
print("number is ", a[1])

#print(user.get("df","phone number is 98062"))
#print(user.get("goo","phone number is 98449"))

# phone number is 98062
# phone number is 98449



user = {
    "name":"Sudan",
    "phone":[
        {
            "type":"Ntc",
            "number":"98449"
        },
        {
            "type":"Ncell",
            "number":"98062"
        }
    ]
}

# Ntc number is 98449
# Ncell number is 98062

print(user.get("phone")[0]['number'])
print(user.get("phone")[1]['number'])

print("Ntc number is", a[1])
print("ncell number is",a[0])


phone = user.get("phone")
print(phone)
phone1 = phone[0]
phone2 = phone[1]

print(f"{phone1['type']} number is {phone1['number']}" )
print(f"{phone2['type']} number is {phone2['number']}" )

print(user.keys())
print(user.values())

#given a nested dictionary representing student data(e.g.names as keys and another dict of subject:marks),how would you extract all students who scored more than 80 in math?




students = {
    "Ram": {"Math": 87, "Science": 75},
    "Sita": {"Math": 75, "Science": 95},
    "Sushant": {"Math": 90, "Science": 80},
    "Anna": {"Math": 60, "Science": 89}
}

high_math_scorers = [name for name, subjects in students.items() if subjects.get("Math", 0) > 80]

print(high_math_scorers)














#Given two dictionaries with overlapping keys, how would you combine them by summing the values of common keys?


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}


result={}

result['a']=dict1.get("a",0)+dict2.get("a",0)
result['b']=dict1.get("b",0)+dict2.get("b",0)
result['c']=dict1.get("c",0)+dict2.get("c",0)
print(result)