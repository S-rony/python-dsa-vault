def number(n):
    if n == 1:
        print(1)
        return
    print(n)
    number(n-1)

number(5)