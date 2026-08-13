def fact(n):
    if n == 0 or n == 1:
        return 1 #fact 0 = 1 and fact 1 = 1 base case
    return n + fact(n-1)


print(fact(5))