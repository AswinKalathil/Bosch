list = [1,2,5,6,8,-2**100]
minn = float("inf")
maxn = float("-inf")
for i in list:
    minn = min(minn,i)
    maxn = max(maxn,i)
    
print("Maximum number from list is: ",maxn)
print("Minimum  number from list is: ",minn)

print(max(list))
print(min(list))