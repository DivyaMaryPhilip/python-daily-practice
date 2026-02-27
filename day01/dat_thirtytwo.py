"""Day 32 – Min Stack (Design Problem)
Design a stack that supports:

push(x)

pop()

top()

getMin()

All in O(1) time."""

stack = []
min_stack = []

def push(n):
    stack.append(n)
    if not min_stack or n<=min_stack[-1]:
        min_stack.append(n)

def pop():
    if not stack:
        return
    if stack[-1] == min_stack[-1]:
        min_stack.pop()
    stack.pop()

def top():
    return stack[-1]

def getmin():
    return min_stack[-1]

if __name__ == "__main__":
    push(5)
    push(2)
    pop()
    top()
    getmin()

    print(top())
    print(getmin())