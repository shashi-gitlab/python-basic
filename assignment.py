# 1) Write a Python script to concatenate following dictionaries to create a new one

# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50, 6:60}
# print(dict1)

# dict1.update(dict2)
# dict1.update(dict3)

# print(dict1)

# ----------------------------------------------------------------------------------------------------------------------------
# 2) Write a Python script to check whether a given key (age) already exists in a dictionary.

# dict1={"name":"dhruv",'age':17,"location":"mumbai"}
# print("age" in dict1)

# ----------------------------------------------------------------------------------------------------------------------------
# 3) Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# n = 5
# dictionary = {x: x*x for x in range(1, n+1)}
# print(dictionary)

# ----------------------------------------------------------------------------------------------------------------------------
# 4) Write a Python script to merge two Python dictionaries.
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# newDict = d1.copy()
# newDict.update(d2)
# print(newDict)

# ----------------------------------------------------------------------------------------------------------------------------
# 5) Write a Python program to iterate over dictionaries using for loops.
# -- fetch values , fetch keys & fetch both

# d = {'Red': 1, 'Green': 2, 'Blue': 3}

# for key in d:
#     print(key)

# for val in d.values():
#     print(val)

# for key, val in d.items():
#         print(key, val)

# ----------------------------------------------------------------------------------------------------------------------------
# 6) Write a Python program to sum all the items in a dictionary.
# my_dict = {'data1':100,'data2':-54,'data3':247}

# sum = 0
# for val in my_dict.values():
#     sum +=val

# print(sum)

# ----------------------------------------------------------------------------------------------------------------------------
# 7) Write a Python program to multiply all the items in a dictionary
# my_dict = {'data1':12,'data2':3, 'data3':4}
# sum = 0
# for val in my_dict.values():
#     if(sum == 0):
#         sum = val
#     else:
#         sum *=val

# print(sum)

# ----------------------------------------------------------------------------------------------------------------------------
# 8) Write a Python program to remove a key from a dictionary. & remove key a from the same

# myDict = {'a':1,'b':2,'c':3,'d':4} 
# del my_dict["a"]
# print(myDict)
# myDict.pop('a')
# print(myDict)

# ----------------------------------------------------------------------------------------------------------------------------
# 9) Write a Python program to get the maximum and minimum value in a dictionary.
# my_dict = {'x':500, 'y':5874, 'z': 560}
# minVal = float('inf')  # Set to positive infinity for finding minimum.
# maxVal = float('-inf')  # Set to negative infinity for finding maximum.

# for val in my_dict.values():
#     if val > maxVal:
#         maxVal = val
#     if val < minVal:
#         minVal = val

# print("min:", minVal, "max:", maxVal)

# ----------------------------------------------------------------------------------------------------------------------------
# 10) Write a Python program to remove duplicate values from Dictionary.
input = {'x':100, 'y':200, "z":300, "a":100}
unique_dict = {}
seen_values = set()
for key, value in input.items():
    if value not in seen_values:
        unique_dict[key] = value
        seen_values.add(value)

print(unique_dict)