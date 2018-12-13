c = 2
d = 1
L = []

for i in range(5):
    if c ** 2 == L[i]:
        print(i)
    else:
        L.append(c ** 2)
        continue
