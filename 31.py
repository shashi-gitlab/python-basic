days = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'fri','sat')

result = []
print(days)
print(result)

for val in days:
    if val == 'fri' or val == 'Mon':
        result.append(val)


print(result)
print(tuple(result))