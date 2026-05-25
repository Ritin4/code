'''
Problem: Prefix sum of a list.
Input: list of numbers 
Output: prefix sum list
'''

def prefix_sum(arr):
    if not arr:
        return []
  
    prefix_list = []
    sum_val = 0

    for num in arr:
        if not isinstance(num, (int, float)):
            raise ValueError("Value is not of type interger or float")

        if isinstance(num, bool):
            raise ValueError("Boolean is not a valid integer")

        sum_val += num
        prefix_list.append(sum_val)
    return prefix_list

print(prefix_sum([]))
print(prefix_sum([1,2,3,4,5,6,7,8,9,10]))
print(prefix_sum([1,-2,3,4,-5, 0]))
print(prefix_sum([True, False]))
print(prefix_sum(["True", "False"]))



