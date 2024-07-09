class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def is_empty(self):
        return not self.stack


if __name__ == "__main__":
    stack = Stack()
    stack.push(42)
    stack.push(10)
    print(stack.top())  # 10
    print(stack.pop(), stack.pop())  # 10 42
    print()

    for i in range(10):
        stack.push(i)

    stack2 = Stack()
    print(stack.stack)
    while not stack.is_empty():
        stack2.push(stack.pop())

    print(stack2.stack)
