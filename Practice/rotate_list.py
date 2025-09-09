lst =[1,2,3,4,5]
d=2
n=len(lst)
d = (d % n)+1

print(lst[d:] + lst[:d])

