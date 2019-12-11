name = input("Input your name: ")


def greet_user(var1, var2):
    print(f"Hi {name} welcome 😀")
    print(f'You log in at: {var1, var2}')


greet_user("14 Jun 2018", "19 Aug 2019")


def square(number):
    return number * number

print(square(3))

from functools import reduce
n = [4, 3, 2, 5]
print(list(map(lambda x: x**2, n)))     # print([x**2 for x in n])
print(list(filter(lambda x: x>2, n)))   # print([x for x in n if x>2])
print(reduce(lambda x, y: x*y, n))