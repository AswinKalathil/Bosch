class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedListNode :
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

    def printLinkedList(self):
        print("Nodes in Linked List")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
          


ll = SinglyLinkedListNode()
ll.append(5)
ll.append(7)
ll.append(4)
ll.append(8)
ll.append(3)
ll.printLinkedList()