def count_occurance(arr, n):
    count = 0 
    for i in arr:
        if i == n:
            count += 1
    print("count: ",count)
    return count

count_occurance([1,2,2,3,4,5,1,6,3,2,2,1], 2)