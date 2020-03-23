class minStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        return len(self.stack)

    def pop(self):
        top = self.stack[len(self.stack)-1]
        self.stack = self.stack[:len(self.stack)-1]
        return top

    def top(self):
        return self.stack[len(self.stack)-1]

    def getMin(self):
        return min(self.stack)

    def display(self):
        print(self.stack)

x = minStack()
x.push(2)
x.push(-2)
print(x.top())
x.display()
print(x.getMin())
