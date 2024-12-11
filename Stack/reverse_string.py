class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

def reverse_string(input_string):
    stack = Stack()

    # Push all characters onto the stack
    for char in input_string:
        stack.push(char)

    # Pop characters from the stack and form the reversed string
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

if __name__ == "__main__":
    input_string = input("Enter a string to reverse: ")
    reversed_str = reverse_string(input_string)
    print(f"Reversed string: {reversed_str}")
