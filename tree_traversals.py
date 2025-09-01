class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def preorder(root):
    if root:
        print(root.key, end=" ")   # 1. Visit root
        preorder(root.left)        # 2. Traverse left
        preorder(root.right)       # 3. Traverse right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key,end=" ")
# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
print("\nPreorder Traversal:")
preorder(root)
print("\nInorder Traversal:")
inorder(root)
print("\nPostorder Traversal:")
postorder(root)