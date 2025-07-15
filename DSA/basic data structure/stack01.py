# Implementing stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())
stack.push(10)
stack.push("Cat")
print(stack.peek())
stack.push(True)
print(stack.size())
print(stack.is_empty())
stack.push(2.2)
print(stack.pop())
print(stack.pop())
print(stack.size())
