def find_max():
    list_of_num = []
    num = int(input("Enter number of elements in list: "))
    for i in range(1, num + 1):
        ele = int(input("Enter elements: "))
        list_of_num.append(ele)
    return max(list_of_num)
