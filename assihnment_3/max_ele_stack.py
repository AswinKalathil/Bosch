# Sample Input

# STDIN   Function
# -----   --------
# 10      operations[] size n = 10
# 1 97    operations = ['1 97', '2', '1 20', ....]
# 2
# 1 20
# 2
# 1 26
# 1 20
# 2
# 3
# 1 91
# 3
# Sample Output

# 26
# 91

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):

    stack =[]
    for op in operations:
        curr_op = op.split(' ')
      
        if curr_op[0] == '1':
            stack.append(int(curr_op[1]))
        elif curr_op[0] =='2':
            stack.pop()
        elif curr_op[0]=='3':
            print(max(stack))
        
            
        

if __name__ == '__main__':
    

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    