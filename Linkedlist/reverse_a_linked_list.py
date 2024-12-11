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

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

if __name__ == "__main__":
    ll = Linkedlist()
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input(f"Enter element{i+1}: "))
        ll.append(data)
    print("Original Linked List: ")
    ll.display()
    ll.reverse()
    print("Reversed Linked List: ")
    ll.display()