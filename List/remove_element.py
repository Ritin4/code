'''
Problem: Function to remove an element at a given index.
Input: Array , index 
Output: Array without the element mentioned at index
'''

def remove_element(arr, index):
    if not arr:
        return "Array should not be empty"

    if index > len(arr) - 1 or index < 0:
        return "Index out of given array's bound"
    
    arr.pop(index)

    return arr

print(remove_element([5, 1, 7, 2], 2))      #Normal case  -- [5, 1, 2]   
print(remove_element([10, 20, 30], -1))     #Negative index -- Index out of given array's bound
print(remove_element([11], 0))              #Single element -- []
print(remove_element([5, 1, 5, 2], 2))      #Duplicate elements -- [5, 1, 2]
print(remove_element([3, 4, 5, 6], 3))      #removing last element -- [3, 4, 5]
print(remove_element([1, "x", 3.5, True], 2)) #Mixed type arrays -- [1, 'x', True]
print(remove_element([10, 20, 30], 3))      #Index larger than array  -- Index out of given array's bound
print(remove_element([], 0))                #Empty array -- Array should not be empty


'''
Obeservations: 

 - Valid rray indices are upto 'len(arr)-1' and not len(arr) since index starts at 0 not 1

 - arr.remove() method removes the first element in the array but not at index 
        Input array: [5, 1, 5, 2]

        Index: 2 (the second 5)
        Expected: [5, 1, 2]
        Actual: [1, 5, 2] (the first 5 is removed)
    
 - arr.pop(index) remove the element at given index, so duplicates are not a problem
 
 - Python accepts negative index, if the behaviour is not intended 'i < 0' check is necessary 

 - Looping of array is unnecessary as we already know the index

'''