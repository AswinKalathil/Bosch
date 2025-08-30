def fact(num):
    if num == 1:
        return 1
    
    return num * fact(num - 1)


num = int(input("Enter a number for factorial: "))

print("Factorial of "+str(num)+" is "+ str(fact(num)))

