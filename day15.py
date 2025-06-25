from operator import add


def test(*data):
    sum  =0
    for i in data:
        sum = sum + i
    return sum

print(test(1,2,2,5,1,1,12,1,1))



def test2(**data):
    print(data)


test2(name="hello", age=12,role="developer", address="dang")


def test3(*args, **kwargs):
    print(args)
    print(kwargs)

test3(1,2,45,5,name="sudan", subject="com")



# args= arbitary positional arguments
# kwargs=arbitary keyboard arguments




