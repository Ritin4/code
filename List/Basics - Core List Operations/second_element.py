'''
Problem: Given a list, return every second element.
Input: list of elements.
Output: list of every second element.
'''

def second_element(arr):

    op_arr = []
    for i in range(1, len(arr), 2):
        op_arr.append(arr[i])

    return op_arr

print(second_element([1,2,3,4,5,6,7]))
print(second_element([]))
print(second_element([0]))
print(second_element(["a"]))
print(second_element(["a", True , False, 12.4, 3]))
print(second_element([0,1]))
print(second_element([1,1,1,2,2,2,6,7]))





