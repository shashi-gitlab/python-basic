# 1) Write a Python program to find last item from the list
# e.g: ["mayank","rahul","rohan","ritik"]

# nameList =  ["mayank","rahul","rohan","ritik"]
# print(nameList)
# to find last item from the list

# lastItem = nameList[-1]
# print(lastItem)

# 2) Write a Python program to check that "rohan" is exist or not & if exist then print "yes"
# e.g: ["mayank","rahul","rohan","ritik"]

# isExist = 'rohan' in nameList
# print(isExist)


# 3) Write a Python program to add new item in the list at the end of the list ( add Akshay at the end)
# e.g: ["mayank","rahul","rohan","ritik"]

# nameList.append('Akshay')
# print(nameList)

# 4) Write a Python program to add new item in the list at 2nd position.
# ( add Akshay at 2nd position)
# e.g: ["mayank","rahul","rohan","ritik"]

# nameList.insert(2,'Akshay')
# print(nameList)

# 5) Write a Python program to delete last value from tuple
# e.g: ["mayank","rahul","rohan","ritik","akshay"]

# newNameList = nameList
# newNameList.pop()
# print(newNameList)

# 6) Write a Python program to delete specific value from tuple i.e. "rahul" in this case
# e.g: ["mayank","rahul","rohan","ritik","akshay"]

# del newNameList[2]
# print(newNameList)

# 7) Write a Python program to delete "3rd" position value from tuple
# e.g: ["mayank","rahul","rohan","ritik","akshay"]

# del newNameList[3]
# print(newNameList)


# 8) Write a Python program to add 2 different list into single list
# e.g: list1 = ["mayank","rahul","rohan"] , list2=["ritik","akshay"]
# Answer: ["mayank","rahul","rohan","ritik","akshay"]

# list1 = ["mayank","rahul","rohan"] 
# list2=["ritik","akshay"]
# ans = list1 + list2
# print(ans)


# 9) Write a Python program to extract last value from the list using negative index number

# e.g: ["mayank","rahul","rohan","ritik","akshay"]
# Answer:akshay

# listVal = ["mayank","rahul","rohan","ritik","akshay"]
# print(listVal[-1])


# 10) Write a Python program to extract first 3 values from the list using range
# i.e( list1[0:4])

# listVal = ["mayank","rahul","rohan","ritik","akshay"]
# print(listVal[:3])

# 11) Write a Python program to extract last 3 values from the list using range

# listVal = ["mayank","rahul","rohan","ritik","akshay"]
# print(listVal[-3:])

# 12) Write a Python program to find total length of the list
# listVal = ["mayank","rahul","rohan","ritik","akshay"]
# print(len(listVal))

# 13) Write a Python program to make your list empty
# list = ["mayank","rahul","rohan","ritik","akshay"]
# list.clear()
# print(list)

# 14) Write a Python program to make delete your list
# list = ["mayank","rahul","rohan","ritik","akshay"]
# del list
# print(list)


# 15) Write a Python program to change item at position 1

list = ["mayank","rahul","rohan","ritik","akshay"]
list[1] = 'abhi'
print(list)