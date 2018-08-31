
def unique(uniqList):

    unique_list = []
    for x in uniqList:
        if x not in unique_list:
            unique_list.append(x)

    for x in unique_list:
        print(x)

numbers = [1, 11, 34, 11, 52, 61, 1, 34]

print("Original list: [1, 11, 34, 11, 52, 61, 1, 34]")
print("Unique list: ")
unique(numbers)