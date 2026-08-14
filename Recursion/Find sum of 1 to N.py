def sum(n):
     #sum of n = n + function of sum(n-1)
    if n == 1:
        print(f"{n} + {0}")
        return 1
    s = n + sum(n-1)
    print(f"{n} + {s}")
    return s

sum(8)

