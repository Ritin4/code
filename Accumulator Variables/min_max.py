def min_max(arr):

    if not arr:
        raise ValueError("Array must not be empty")

    min_val = arr[0]
    max_val = arr[0]

    for ele in arr:
        if ele < min_val:
            min_val = ele
        if ele > max_val:
            max_val = ele
         
    print("Min: " , min_val)
    print("Max: " , max_val)

    return min_val, max_val
 
min_max([21,54,75,23,78,24,11])
# min_max([])



#Note: max and min cannot be used as variable names as they have predefined functionality in python.


# In Python, the built-in functions max() and min() are used 
# to find the largest and smallest items, respectively,
# in an iterable (such as a list, tuple, or string), 
# or to compare two or more arguments. 


