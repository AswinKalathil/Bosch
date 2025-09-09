def is_balanced(brackets: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}  

    for c in brackets:
        if c in "({[":
            stack.append(c)   
        elif c in ")}]":
            if not stack:     
                return False
            if stack.pop() != pairs[c]: 
                return False
        else:
            return False  

    return len(stack) == 0  


print(is_balanced("{[{()}]}"))   
print(is_balanced("{[(])}"))    
print(is_balanced("((("))        
