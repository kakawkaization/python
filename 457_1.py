S = 'hello'

arr = []
arr1 = []
sum = 0
for i in S:
    sum += ord(i)
    arr.append(ord(i))

print('Sum of characters:', sum)
print('List of characters:', arr)
print('List of characters with map function:',list(map(ord, S)))
