user1 = {"user1", "user2","user4","user3"}
user2 = user1
print(user1)
print(user2)

user2.remove("user2") #this will effect in both valiable because they both have same memory allocation
print(user1)
print(user2)