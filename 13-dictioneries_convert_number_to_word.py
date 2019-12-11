customer = {
    "name": "John Smith",
    "age": 30,
    "phone number": 9121212223
}

customer["name"] = "Rich Bach"
customer["birthdate"] = "Jan 13 1980"
print(customer["birthdate"])

convert_digit_to_word = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
get_number = input("Enter your phone number: ")
output = ""
for number in get_number:
    output += convert_digit_to_word.get(number, "!") + " "
print("Your number is:", output)
