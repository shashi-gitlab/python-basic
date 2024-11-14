# get value from set

users = {"user1", "user2","user4","user3"}
# print(users[0]) # this will give error  beacuse set has not index format

print("user2" in users)


# this the the way how we can get value
for val in users:
    print(val)