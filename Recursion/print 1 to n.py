#print 1 to n
def number(n):
    if n == 1:
        print(1)
        return
    number(n-1)
    print(n)

number(5)