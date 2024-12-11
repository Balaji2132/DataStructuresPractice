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

    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next distinct node
                current = current.next

if __name__ == "__main__":
    ll = Linkedlist()
    n = int(input("Enter the number of elements: "))
    print("Enter elements in sorted order:")
    for i in range(n):
        data = int(input(f"Enter element {i + 1}: "))
        ll.append(data)
    print("Original Linked List:")
    ll.display()
    ll.remove_duplicates()
    print("Linked List after removing duplicates:")
    ll.display()
#TODO: Sort in the code and do not ask for the sorted input