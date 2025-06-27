# Recursion

# a = [1,2,3,4,[5,6,[7,[8,[9]]]]]
# a = [1,2,3,4,5,6,7,8,9]

def flatten_list(n):
    result = []
    for i in n:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
a = [1, 2, 3, 4, [5, 6, [7, [8, [9]]]]]
result= flatten_list(a)
print(result)



a = lambda *args : list(args)
print(a(1,2,3,4,5))

data = {
    "name":"sudan",
    "address":"dang"
}


values = []
for i in data.values():
    values.append(i)

print(values)

values = [i for i in data.values()]
print(values)

lambda_data = lambda data: [i for i in data.values()]


def lamda_data(data):
    values = []
    for i in data.values():
        values.append(i)
    return values