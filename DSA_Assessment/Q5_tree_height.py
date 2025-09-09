class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def height(root):
    if not root:
        return -1
    return max(height(root.left),height(root.right))+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.left.right.right = Node(6)

print("Height of tree: ",height(root))

