def left_rotate(arr, d):
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]


arr = [1,2,3,4,5]
d = 2
print("Array Before rotation: ",arr)
print("Array After :",d," rotation", left_rotate(arr, d))
