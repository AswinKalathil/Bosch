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
# print(ll.get_node_at(int(input())))
ll.preppend(0)
ll.display()
ll.delete_node_by_value(3)
ll.display()

