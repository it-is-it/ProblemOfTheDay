# 232. Implement Queue using Stacks
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false


class MyQueue:
    def __init__(self):
        # Initialize two stacks
        self.stack1 = []  # Main stack for push operations
        self.stack2 = []  # Auxiliary stack for pop and peek operations

    def push(self, x: int):
        # Push the element onto stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # Ensure stack2 has the current front of the queue
        self._move_stack1_to_stack2()
        return self.stack2.pop()

    def peek(self) -> int:
        # Ensure stack2 has the current front of the queue
        self._move_stack1_to_stack2()
        return self.stack2[-1]

    def empty(self) -> bool:
        # The queue is empty if both stacks are empty
        return not self.stack1 and not self.stack2

    def _move_stack1_to_stack2(self):
        # Move elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


# Test case based on the provided example
operations = ["MyQueue", "push", "push", "peek", "pop", "empty"]
inputs = [[], [1], [2], [], [], []]

# Initialize queue
myQueue = None
results = []

for i, operation in enumerate(operations):
    if operation == "MyQueue":
        myQueue = MyQueue()
        results.append(None)
    elif operation == "push":
        myQueue.push(inputs[i][0])
        results.append(None)
    elif operation == "pop":
        results.append(myQueue.pop())
    elif operation == "peek":
        results.append(myQueue.peek())
    elif operation == "empty":
        results.append(myQueue.empty())

# Output results
print("Results:", results)