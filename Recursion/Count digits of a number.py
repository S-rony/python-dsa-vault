def count_digit(num):
    count = 1
    if num == 0:
        return 0
    elif num // 10 == 0:
        return 1

    count = count + count_digit(num // 10)
    return count

print(count_digit(100001))
