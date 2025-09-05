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


def search(root,key):
    
    if not root or root.key == key  :
        return root
    elif root.key > key:
        return search(root.left,key)
    else:
        return search(root.right,key)
    



def inorder(root):
    if root:
        
        inorder(root.left)
        print(root.key,end =" ")
        inorder(root.right)

def postorder(root):
    if root:
        
        postorder(root.left)
        postorder(root.right)
        print(root.key,end =" ")

def preorder(root):
    if root:
        print(root.key,end =" ")
        preorder(root.left)
        preorder(root.right)
        

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
r = insert(r,1)
r = insert(r,2)
r = insert(r,3)
r = insert(r,4)

print("Inorder Traversal")
inorder(r)
print("\nPostorder Traversal")
postorder(r)
print("\nPreorder traversal")
preorder(r)
print("")
print("Searching 10 ")
print("Found" if search(r, 10) else "Not Found")
print("Searching 80 ")
print("Found" if search(r, 80) else "Not Found")


