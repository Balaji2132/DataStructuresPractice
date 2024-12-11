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

def evaluate_postfix(expression):
    stack = Stack()

    # Iterate over each character in the expression
    for char in expression:
        if char.isdigit():  # If the character is a digit, push it onto the stack
            stack.push(int(char))
        else:
            # Pop two operands for the operator
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Perform the operation and push the result back onto the stack
            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 // operand2)  # Integer division

    # The result is the last item in the stack
    return stack.pop()

if __name__ == "__main__":
    postfix_expr = input("Enter a postfix expression (e.g., '231*+9-'): ")
    result = evaluate_postfix(postfix_expr)
    print(f"The result of the postfix expression '{postfix_expr}' is: {result}")
