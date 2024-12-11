class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def find_middle(self):
        # Use two pointers: slow and fast
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next  # Move slow by one step
            fast = fast.next.next  # Move fast by two steps
        return slow  # Slow will point to the middle node

if __name__ == "__main__":
    ll = Linkedlist()
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input(f"Enter element {i + 1}: "))
        ll.append(data)
    print("Original Linked List:")
    ll.display()
    middle_node = ll.find_middle()
    if middle_node:
        print(f"The middle node is: {middle_node.data}")
    else:
        print("The linked list is empty.")
