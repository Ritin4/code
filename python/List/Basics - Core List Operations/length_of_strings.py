'''
Problem: Given a list of strings, return list of lengths of strings.
Input: list of strings.
Output: list of lengths of string.
'''

def length_of_string(arr):

    len_arr = []
    for string in arr:

        if not isinstance(string, str):
            continue

        len_arr.append(len(string))
    
    return len_arr

print(length_of_string(["dog", "cat", "sheep"]))
print(length_of_string([]))
# print(length_of_string(["dog", "cat", 3]))
# print(length_of_string(["dog", "cat", True]))
print(length_of_string(["a", None]))
print(length_of_string(["hello", 123]))
print(length_of_string(["test", ["nested"]]))
print(length_of_string(["hello", 123]))
print(length_of_string([True, "false"]))
print(length_of_string([b"bytes"]))
print(length_of_string(["ok", {"key": "value"}]))








