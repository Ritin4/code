'''
Problem: count the occurance of a value in given array.
Input: Array , element  
Output: Frequency / Count of the element in array
'''

def count_occurance(arr, ele):

    count = 0
    for i in arr:
        if i == ele:
            count += 1
    return count 

print(count_occurance([1,2,11,1,4,5,1,1],1))
print(count_occurance([],1))
print(count_occurance([1,2,3,4,5],6))

'''
Observations:

- If a empty check for arrays is provided, [] empty array test case fails as it doesn't return the count

    # Expected output: 0
    # Actual output: "Array cannot be empty"
    count_occurance([], 5)
'''

