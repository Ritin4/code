'''
Problem: Given a list of integers, return the list of squares
Input: array of integers 
Output: list of squares
'''

def squares_list(arr):

    sqr_lst = []

    if not arr:
        raise ValueError("Array cannot be empty") 

    for ele in arr:
        if isinstance(ele, bool):
            raise ValueError("Boolean is not a valid integer")

        if not isinstance(ele,  int):
            raise ValueError("Not a valid integer")
        
        sqr = ele ** 2
        sqr_lst.append(sqr)
         
    return sqr_lst

print(squares_list([1,2,3]))
print(squares_list([0,1,2,3,-4]))
print(squares_list([]))
print(squares_list(['0',1,2,3,-4]))
print(squares_list([0]))
print(squares_list([1]))
print(squares_list([0]))
print(squares_list([999999]))
print(squares_list([-999999]))
print(squares_list([1, 2.2, 3]))
print(squares_list([True, False]))
print(squares_list([float("inf")]))
print(squares_list([float("man")]))


'''
Observations:

- ***Boolean values pass isinstance(True, int) because they are subclasses of int. 
- Using ele *= ele modifies the loop variable instead of computing ele ** 2, which is less clear.

'''









