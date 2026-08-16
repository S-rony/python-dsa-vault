#Method loop

def fact_iterative(n):
    result = 1
    for i in range(2,n+1):
        result = result * i
    return result

print(fact_iterative(5))

#Method recursive
def fact_(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_(n-1)

print(fact_(5))