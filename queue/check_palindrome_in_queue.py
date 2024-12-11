from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def is_palindrome(self, string):
        # Check if a string is a palindrome
        return string == string[::-1]

    def find_palindromes(self):
        palindromes = [item for item in self.queue if self.is_palindrome(item)]
        return palindromes

if __name__ == "__main__":
    q = Queue()
    n = int(input("Enter the number of items to add to the queue: "))
    for _ in range(n):
        item = input("Enter a string: ")
        q.enqueue(item)

    palindromes = q.find_palindromes()

    if palindromes:
        print(f"The queue contains the following palindromes: {', '.join(palindromes)}")
    else:
        print("There are no palindromes in the queue.")
