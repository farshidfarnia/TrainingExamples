my_family = ["Farshid", "Elham", "Avina", "Arshida"]
print(my_family[3])
print("-^-" * 20)

# Method 1 : Sort the list in ascending order and print the last element in the list.
numbers = [10, 20, 32, 1, 9, 3, 108, 5, 1]
numbers.sort()
print('Largest element in this list is:', numbers[-1])
print("-^-" * 20)

# Method 2 : Using max() method
print('Largest element in this list is:', max(numbers))
print("-^-" * 20)

# Method 3 : Find max list element on inputs provided by user
list_of_num = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list_of_num.append(ele)

print("\nLargest element is:", max(list_of_num))
