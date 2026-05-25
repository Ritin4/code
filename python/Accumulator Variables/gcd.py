"""
greatest common divisor is the largest number which can be 
derived from the divisors of given numbers and the divisor
can divide all the given numbers without leaving the remainder

"""

'''
Algorithm: 
    1. find out facotrs of m
    2. find out factors of n
    3. fing the largest number common between the factors of m and n
'''

def gcd(m,n):
    cf = []
    for i in range(1, min(m,n)+1):
        if m%i==0 and n%i==0:
            cf.append(i)
    return cf[-1]

print(gcd(8,24))
