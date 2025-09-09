import sys 
min_n = 2**31
max_n = -2**31
for k in range(1,len(sys.argv)):
    min_n=min(min_n,int(sys.argv[k]))
    max_n=max(max_n,int(sys.argv[k]))
print("Minimum of arguments",min_n)  
print("Maximum of arguments",max_n)