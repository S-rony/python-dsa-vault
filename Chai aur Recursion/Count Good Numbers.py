# A digit string is good if the digits (0-indexed)
# at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

# For example, "2582" is good because the digits (2 and 8) at even positions are even and
# the digits (5 and 2) at odd positions are prime.
# However, "3245" is not good because 3 is at an even index but is not even.

# Given an integer n, return the total number of good digit strings of length n.
# Since the answer may be large, return it modulo 109 + 7.(10 power 9 + 9 ) -> 10 digit  prime number

# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

#secret handshake problems


# numbers = 0 - 9
# even position -> even number = 0,2,4,6,8
# odd position ->prime number = 2,3,5,7

#input if 4 digits are there means 4 spaces for the digits? output ??
# - - - -  >>> 4 spaces
#0th index - _ even position 5 options
#1st index - _ odd 4 options
#2nd index - _ even position 5 options
#3rd index - _ odd 4 options
# output will be = 5 * 4 * 5 * 4 = 400
# 5power(2) X 4power(2) = 400 or  5power(even) X 4power(odd) = 400

'''----------------------------------------------------------------'''
"""MOD = 10**9 + 7

def power(x, n , mod):
    if n == 0:
        return 1
    half = power(x,n//2, mod)
    result = (half * half) % mod
    if n % 2 == 1:
        result = (result * x) % mod
    return result

def count_good_strings(n):
    even_count = (n + 1) // 2
    odd_count = n // 2

    return(pow(5,even_count, MOD) * pow(4,odd_count, MOD)) % MOD"""

'''------------------------------------------------------------------'''


class Solution:
    MOD = 10 ** 9 + 7

    @staticmethod
    def power(x, n, mod):
        if n == 0:
            return 1
        half = Solution.power(x, n // 2, mod)
        result = (half * half) % mod
        if n % 2 == 1:
            result = (result * x) % mod
        return result

    def countGoodNumbers(self, n: int) -> int:
        even_count = (n + 1) // 2
        odd_count = n // 2

        return (self.power(5, even_count, self.MOD) * self.power(4, odd_count, self.MOD)) % self.MOD