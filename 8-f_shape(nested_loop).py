numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print("X" * x)

print("-^-" * 20)

for y in numbers:
    output = ""
    for count in range(y):
        output += "x"
    print(output)

print("-^-" * 20)

new_list = [2, 2, 2, 2, 7]
for x in new_list:
    print("X" * x)