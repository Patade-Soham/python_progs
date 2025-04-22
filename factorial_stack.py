import math
from collections import deque

n = int(input("Enter number for factorial: "))
print("Factorial:", math.factorial(n))

stack = []
stack.append(input("Push to stack: "))
print("Popped:", stack.pop())

queue = deque()
queue.append(input("Enqueue: "))
print("Dequeued:", queue.popleft())
