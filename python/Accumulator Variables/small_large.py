#Program to track two smallest and two largest elements in array
#Author: Ritin

def small_large(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
        
    min1 = min2 = float("inf")
    max1 = max2 = float("-inf")

    for x in arr:

        #updating the minimum numbers
        if x < min1:
            min1 = x
        elif x < min2:
            min2 = x

        #updating the maximum numbers
        if x > max1:
            max1 = x
        elif x > max2:
            max2 = x

    print("min1", min1)
    print("min2", min2)
    print("max1", max1)
    print("max2", max2)

    return min1, min2, max1, max2

small_large([21,54,75,23,78,24,11])