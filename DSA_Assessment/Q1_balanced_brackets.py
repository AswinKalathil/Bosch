def is_valid(s):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    for ch in s:
        if ch in pairs:
            top = stack.pop() if stack else '#'
            if pairs[ch] != top:
                return "NO"
        else:
            stack.append(ch)
    if not stack:
        return "YES"
    else:
        return "NO"

input1 = "({{[]}})"
input2 = ")){}"

print("Is this valid ",input1," ",is_valid(input1))  
print("Is this valid ",input2," ",is_valid(input2))      
