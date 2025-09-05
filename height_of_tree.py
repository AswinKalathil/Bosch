class Node:
    def __init__(self,key):

        self.key = key
        self.left=None
        self.right = None
def insert(root,key):
    if not root:
        return Node(key)
    if root.key == key:
        return root
    elif root.key > key:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    
    return root

def height(root):
    if not root:
        return -1
    return max(height(root.left),height(root.right))+1

# create root
r1 = Node(50)

# left child
r2 = Node(40)
r1.left = r2

# right child
r3 = Node(60)
r1.right = r3

# children of 40
r4 = Node(30)
r5 = Node(45)
r2.left = r4
r2.right = r5



print(height(r1))

root = Node(1)
current = root
for i in range(2, 11):   # 2 to 10
    current.right = Node(i)   # insert as right child
    current = current.right

print(height(root))    