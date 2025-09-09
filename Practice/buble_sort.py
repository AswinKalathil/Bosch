listn = [5,3,2,3,3,5,5,3,9,66,7,5,8]
n = len(listn)
for i in range(n):
    
    for j in range(n-i-1):
        if listn[j] > listn[j+1] :
            listn[j],listn[j+1] = listn[j+1],listn[j]
print(listn)            