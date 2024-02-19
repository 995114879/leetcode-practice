from collections import deque
stack = deque()
p = input()
for i in p:
    stack.append(i)
s = ""
for e in reversed(stack):
    s += e
print(float(s))