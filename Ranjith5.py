list1 = [11, 22, 33, 44, 55]
list2 = [44, 55, 66, 77, 88]
list3 = [55, 66, 77, 88, 99]

duplicates = set(list1) & set(list2) & set(list3)

print(f"The duplicates in the three lists are {list(duplicates)}.")