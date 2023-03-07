from collections import deque

l = deque()
l.append(5) # to inseert from right
l.appendleft(6) # to insert from left
l.append(7)
l.append(10)
print(l[2])
