def number(string, left, right):
    l = list(string)
    if  right <= left:
        return l
    l[left], l[right] = l[right], l[left]
    return number(l,left + 1, right - 1)

string = "name"
left = 0
right = len(string) - 1
print(number(string,left,right))

