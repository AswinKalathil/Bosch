class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

def traverse(head):

    current_node = head

    while current_node:

        print(current_node.data,end =" --> ")
        current_node = current_node.next
    print("Null")
def min_node_data(head):
    curr_node = head
    min_data = head.data

    while curr_node:

        min_data = min(min_data,curr_node.data)
        curr_node = curr_node.next
    return min_data

def max_node_data(head):
    curr_node = head
    max_data = head.data

    while curr_node:

        max_data = max(max_data,curr_node.data)
        curr_node = curr_node.next
    return max_data
def search_data(head,key):

    curr_node = head

    while curr_node :
        if curr_node.data == key:
            print("Given data ",key,"is FOUND")
            return
        curr_node = curr_node.next
    print("Given data ",key,"is NOT FOUND")


n1 = Node(25)
n2 = Node(5)
n3 = Node(65)
n4 = Node(3)
n5 = Node(9)
n6 = Node(77)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

traverse(n1)
print("Minimum value : ",min_node_data(n1))
print("Maximum value : ",max_node_data(n1))

search_key = int(input("Enter a number: "))
search_data(n1,search_key)

