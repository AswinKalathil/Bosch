listn = [3,6,4,9,2,3,8,5,5,4,3]

counter = {}

for item in listn:
    counter[item] = counter.get(item,0) + 1

print(counter)    


