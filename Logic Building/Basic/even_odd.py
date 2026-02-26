'''
Problem: Check even or odd
Input: number
Output: true if even odd if false 
'''

def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(even_odd(5))
print(even_odd(6))
print(even_odd(-2))
print(even_odd(0))

