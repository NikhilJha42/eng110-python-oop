def multi_args(*multiargs):

    print(type(multiargs))

    for arg in multiargs:
        print(arg)

# multi_args(1, 2, 3, 4, 5, 6, 6, "John")

# def greeting(name: str):
#     print("Hello, my name is " + name)
#
# greeting("Test")

def division(denom: int, num: int) -> float:
    return denom / num

def subtraction(int1: int = 5, int2 = 2) -> int:
    return int1 - int2

print(subtraction(7.5))