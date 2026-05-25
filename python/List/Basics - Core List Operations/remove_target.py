'''
Problem: Remove all occurrences of a target value from a list.
Input: list of elements, target element to remove 
Output: list without the target element
'''

def remove_target(arr, target):
    out_list = []
    if not arr:
        raise ValueError("List cannot be empty!!")

    # for ele in arr:
    #     if ele != target:
    #         out_list.append(ele)

    # return out_list

    for i in range(len(arr)-1 , -1 , -1):
        if arr[i] == target:
            arr.pop(i)

    return arr
    
    

print(remove_target([1,2,1,4,5], 1))
print(remove_target([1, 2, 2, 3], 2))
print(remove_target([True,2,1,False,5], True))
print(remove_target([1], 1))
print(remove_target([1], 0))
print(remove_target([1,"a",3.7,34,"b","a"], "a"))





''' 
Observations:

    # for index, ele in enumerate(arr):
    #     if ele == target:
    #         arr.pop(index)
    #return arr

- The above logic fails as we are changing the list while looping 
- This causes the list to skip elements 
    - Example:
         [1,2,2,3] target=2

        -> i=0
            1 == 2   ->no match
        -> i=1
            2 == 2   ->match

    -now the list becomes [1,2,3], index moves to 2
        
        -> i=2
            3 == 2 ->no match
    
    -here the 2 is getting skipped as the index is modified while looping leading to unintended output 

- ***To handle this scenario we can either create a new list and append the items or iterate the list backwards, 
    so that the index change won't impact the iteration
        
'''
