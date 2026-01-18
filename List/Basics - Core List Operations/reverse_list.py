'''
Problem: Implement min() and max() functions using loops 
Input: array  
Output: min and max elements of given array 
'''

def reverse_list(arr):
    left , right = 0 , len(arr)-1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr


print(reverse_list([1,2,3,4,5,6]))
print(reverse_list([]))
print(reverse_list(["A", 21,True, 33.6]))


