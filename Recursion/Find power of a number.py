def finding_power(n, power):
    if  n == n and power == 0:
        return 1
    elif n == n and power == 1:
        return n

    pow =  finding_power(n,1) * finding_power(n,power -1)
    return pow

print(finding_power(4, 4))


#much cleaner
def pow(n, power):
    if power == 0:
        return 1
    return n * pow(n , power -1)
print(pow(2,1))


