# Design a stack that supports `push`, `pop`, `top`, and retrieving the maximum element in constant time.
# - `push(x)` - Push element `x` onto stack
# - `pop()` - Removes the element on top of the stack
# - `top()` - Get the top element (sometimes referred to as "peek")
# - `get_max()` - Retrieve the maximum element in the stack


stack = []
max = []

def push(x):
    stack.append(x)

    if max:
        if x > max[-1]:
            max.append(x)
    else:
        max.append(x)

def pop():
    if stack[-1] == max[-1]:
        max.pop()

    stack.pop()

def top():
    return stack[-1]

def get_max():
    return max[-1]

push(3)    
push(6)
push(4)
pop()
push(4)
push(8)
push(1)
top()
print(stack)
print(top())
print(get_max())
