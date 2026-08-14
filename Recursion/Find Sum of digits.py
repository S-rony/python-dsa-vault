def sum_of_digits(n):
    if n // 10 == 0 and n % 10 == n:
        return n
    sum = n % 10
    n = n // 10
    return sum + sum_of_digits(n)

print(sum_of_digits(1000078))


