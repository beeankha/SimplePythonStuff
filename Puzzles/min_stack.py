# Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.
# - `push(x)` - Push element `x` onto stack
# - `pop()` - Removes the element on top of the stack
# - `top()` - Get the top element (sometimes referred to as "peek")
# - `get_min()` - Retrieve the minimum element in the stack

stack = []
min = []

def push(x):
    stack.append(x)

    if min:
        if x < min[-1]:
            min.append(x)
    else:
        min.append(x)

def pop():
    if stack[-1] == min[-1]:
        min.pop()

    stack.pop()

def top():
    return stack[-1]

def get_min():
    return min[-1]

push(3)    
push(6)
push(4)
push(8)
pop()
push(1)
pop()
top()
print(stack)
print(top())
print(get_min())

# Failed attempts below!

# def min_stack(value):
#     min_value = []
#     new_list = []
#     new_list.append(value)
#     compare = new_list[0]
#     if compare <= min_value[0]:
#         min_value.pop(0)
#         min_value.append(compare)
        
    # for n in new_list:
    #     min_value.append(n)
    #     x = min_value[0]
    #     if n >= x:
    #         continue
    #     else:
    #         min_value.append(n)
    #         min_value.pop(1)
    # return new_list, min_value

# Things I didn't understand:
# - Supposed to create functions that do the things like append() etc.
# - Need everything to be more flexible
