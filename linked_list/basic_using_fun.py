# Define a function to create a new node
def create_node(data, next_node=None):
    return {"data": data, "next": next_node}

# Define a function to insert at the beginning of the list
def insert_at_begin(head, data):
    new_node = create_node(data)
    new_node["next"] = head
    return new_node

# Define a function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current["data"], end=" -> ")
        current = current["next"]
    print("None")  # Indicates the end of the list

# Initialize an empty linked list (head is None)
head = None

# Insert elements at the beginning
head = insert_at_begin(head, 5)
head = insert_at_begin(head, 10)

# Print the linked list
print_list(head)
