from math import sqrt

raw_list = [2, 4, 9, 16, 25]

new_list = []

print("For:")
for i in raw_list:
    new_list.append(sqrt(i))
print(new_list)

print("Map:")
new_list2 = []

new_list2 = list(map(lambda x: sqrt(x), raw_list))
print(new_list2)

print("Generator lists:")
new_list3 = [sqrt(x) for x in raw_list]
print(new_list3)