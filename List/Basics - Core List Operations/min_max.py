'''
Problem: Implement min() and max() functions using loops 
Input: array  
Output: min and max elements of given array 
'''

def min_max(arr):
    if not arr:
        return "Array cannot be empty"

    min_val = float("inf")
    max_val = float("-inf")

    for ele in arr:

        if not isinstance(ele, (int, float)):
            return f"{ele} is not a valid interger or float"

        if ele < min_val:
            min_val = ele
        elif ele > max_val:
            max_val = ele

    return min_val, max_val

print(min_max([12,34,56]))          #(12, 56)
print(min_max([]))                  #Array cannot be empty
print(min_max([-12,34,56]))         #(-12, 56)
print(min_max([-12,34,-13,56]))     #(-13, 56)
print(min_max([-12,34,-13,56,0]))   #(-13, 56)
print(min_max([0,1,2,3]))           #(0,3)





