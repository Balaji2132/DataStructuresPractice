from collections import deque

def generate_binary_numbers(n):
    # Initialize an empty queue
    queue = deque()
    
    # Enqueue the first binary number
    queue.append("1")
    
    # List to store the binary numbers
    result = []
    
    # Generate binary numbers
    for _ in range(n):
        # Dequeue the front binary number
        front = queue.popleft()
        result.append(front)
        
        # Enqueue the next two binary numbers
        queue.append(front + "0")
        queue.append(front + "1")
    
    return result

if __name__ == "__main__":
    n = int(input("Enter the number of binary numbers to generate: "))
    binary_numbers = generate_binary_numbers(n)
    print("The first", n, "binary numbers are:")
    print(" ".join(binary_numbers))
