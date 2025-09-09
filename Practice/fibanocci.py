def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)
     
#optimized

def fib2(a,b,count,n):
    if count >= n:
        return
    print(a,end =" ")
    fib2(b,a+b,count+1,n)
    
limit = int(input("Enter the limit for fibanocci series: "))

# for i in range(limit):
#     print(fib(i),end=" ")

fib2(0,1,0,limit)