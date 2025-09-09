class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList :
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

def printLinkedList(head):
        print("Nodes in Linked List")
        temp = head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next    
def reverse(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next     
            curr.next = prev   
            prev = curr         
            curr = nxt          
        head = prev 
        return head           
          
ll = SinglyLinkedList()
ll.append(5)
ll.append(7)
ll.append(4)
ll.append(8)
ll.append(3)
printLinkedList(ll.head)
new_head = reverse(ll.head)
print("\nAfter Reverse")
printLinkedList(new_head)


