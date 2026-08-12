from collections import deque
d = deque([10,20,30,40,50])

temp = d.pop()
d.appendleft(temp)

print(d)





