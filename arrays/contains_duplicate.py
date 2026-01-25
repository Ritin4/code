'''
Problem: Given an integer array, return true if any of the element is present at least twice and false if all the elements are distinct
Input: array of integers 
Output: True if there are duplicates, False if all are distinct
'''

def contains_duplicate(arr):
    if not arr:
        return False

    tracker = {}
    
    for num in arr:
        if not isinstance(num, int):
            raise ValueError("Not a valid integer")

        if num not in tracker.keys():
            tracker[num] = 1
        else:
            tracker[num] += 1
        
        print(tracker)


    for count in tracker.values():
        if count > 1:
            return True
    
    return False


print(contains_duplicate([1,2,1,1,1,3,4,5]))