list_of_users = ['Farshid', 'Elham', 'Arshida', 'Avina']
for item in list_of_users:
    print(item)

for item in range(3, 50, 3):
    print(item)
print("-^-" * 20)

prices = [30, 20, 15]
total = 0
for price in prices:
    total += price
print(f'Total: {total}')

# this line is equal the top for loop
print('Total:', sum(prices))