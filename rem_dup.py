list = [5,3,2,3,3,5,8]

copy = []

for i in list:
    if i not in copy:
        copy.append(i)

print(copy)
