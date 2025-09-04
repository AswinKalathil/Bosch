# You are required to implement basic data structures from scratch using Python.
#  Do not use built-in libraries like collections or queue for core logic — write your own implementation.
# Requirements
# 1. Stack (LIFO)
# Implement a class Stack with methods:
# push(item) → add an element to the stack
# pop() → remove and return the top element
# peek() → return the top element without removing it
# is_empty() → check if stack is empty
# size() → return number of elements
# 2. Queue (FIFO)
# Implement a class Queue with methods:
# enqueue(item) → add an element to the queue
# dequeue() → remove and return the first element
# peek() → return the first element without removing it
# is_empty() → check if queue is empty
# size() → return number of elements
# 3. Linked List
# Implement a Singly Linked List with:
# append(data) → add a node at the end
# prepend(data) → add a node at the beginning
# delete(data) → delete a node with given value
# display() → print the linked list
# 4. Binary Search Tree (BST)
# Implement a BST with:
# insert(value) → insert a node
# search(value) → check if value exists
# inorder() → inorder traversal (sorted output)
# preorder() and postorder() → traversal methods
# 5. Dictionary Implementation
# Implement a simple HashMap using Python lists (without using built-in dict):
# put(key, value)
# get(key)
# remove(key)
# Handle collisions using chaining (list of lists).


class Stack:
    def __init__(self):
        self.items =[]
        

    def push(self,ele):
        self.items.append(ele)
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.items.pop()
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,ele):
        self.items.append(ele)
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.items.pop()
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.items.pop()
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):

        new_node = Node(data)

        if not self.head:
            
            self.head = new_node
            return 
        curr = self.head

        while(curr.next):
            curr = curr.next
        curr.next = new_node
    def preppend(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return 
        new_node.next = self.head
        self.head = new_node



    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def get_node_at(self,pos):
        
        curr = self.head
        index=0
        while index < pos and curr.next is not None:
            curr = curr.next
            index +=1
        if index < pos and curr.next is None:
            print("No such position")
            return 
        return curr.data 
    def delete_node_by_value(self,val):
        curr = self.head
        if self.head is None:
            print("Linked list is empty")
            return
        
        if curr.data == val:
            
            self.head = curr.next
            curr = None
            return

        prev = None
        while curr is not None:
        
            if curr.data == val:
                prev.next = curr.next
                curr = None
                return
            prev = curr
            curr = curr.next

        print(f"Value {val} not found in the list")
            


        
        
       
 

ll = LinkedList()
ll.append(1)
ll.append("a")
ll.append(30)
ll.append("l")
ll.append(5)
print("Linked List:")
ll.display()
print(ll.get_node_at(int(input())))
ll.preppend(0)
ll.display()
ll.delete_node_by_value(3)
ll.display()



# ==== Stack Demo ====
print("=== Stack Demo ===")
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element:", stack.peek())   # 30
print("Stack size:", stack.size())    # 3
print("Popped:", stack.pop())         # 30
print("Is empty:", stack.isEmpty())  # False

# ==== Queue Demo ====
print("\n=== Queue Demo ===")
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Front element:", queue.peek())  # A
print("Queue size:", queue.size())     # 3
print("Dequeued:", queue.dequeue())    # A
print("Is empty:", queue.isEmpty())   # False

