#membership operators

a=[1,2,3,4,5]

#in ,
#not in
print(3 in a)
print(7 not in a)
print(7 in a)

#loops
for i in [1,2,3,4,5,6,7]:
    print(i)

for i in ["broadway","education"]:
    print(i)

for i in range(1,10,1):
    print(i)

#range(1,10)=> by default 
#

for i in range(10):
    print(a)

for i in range(1,11,1):
    print(f'2 X {i}={2*i}')

people=[
    {"name":"Salina",
    "dob":"09-19"
    },
    {"name":"Simran",
    "dob":"09-19"
    },
    {"name":"Anjali",
    "dob":"03-02"
    },
    {"name":"Swastika",
    "dob":"10-28"
    }
]
current_date ="03-02"
for i in people:
    if current_date==i['dob']:
        print(f"Happy birthday, {i['name']}")


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

phone=user.get("phone")
print(phone)
current=98449, 98062
for i in phone:
    print(f"{i['type']} number is {i['number']}")



    people=[
    {"name":"Salina",
    "dob":"09-19"
    },
    {"name":"Simran",
    "dob":"09-19"
    },
    {"name":"Anjali",
    "dob":"03-02"
    },
    {"name":"Swastika",
    "dob":"10-28"
    }
]
current_date ="03-02"
for i in people:
    if current_date==i['dob']:
        print(f"Happy birthday, {i['name']}")
