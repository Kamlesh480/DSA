class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Creating an instance of LinkedList and calling insertAtBegin
ll = LinkedList()
ll.insertAtBegin(5)
ll.insertAtBegin(10)

# Call printList to display the linked list
ll.printList()