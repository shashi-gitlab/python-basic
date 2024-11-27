users = {"user1", "user2","user4","user3"}
print(users)

users.discard("user2") # remove last value from set, it could be any value because it unorder format
print(users)

users.discard("user20") # this will check value if exist then remove else do nothing
print(users)

users.remove("user20") # but here if value does not exist in the set it will give error
print(users)