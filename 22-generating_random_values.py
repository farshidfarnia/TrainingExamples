import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

animal = ['bear', 'wolf', 'leopard', 'lion']
print(random.choice(animal))