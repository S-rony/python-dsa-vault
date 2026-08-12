from collections import deque
#palindrome
list = [1,2,3,2,1]
d = deque([1,2,1,2,1])
check = True
left = 0

while d != []:
    right = len(d) - 1
    if len(d) == 1:
        break
    if d[left] == d[right]:
        check = True

        d.pop()
        d.popleft()

    else:
        # print("False No palindrome")
        check = False
        break
# left += 1
# right -= 1

if check:
    print("True")
else:
    print("False")