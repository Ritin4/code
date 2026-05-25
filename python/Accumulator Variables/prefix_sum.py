def prefix_sum(arr):
    op_arr = []
    
    for i in arr:
        if len(op_arr) == 0:
            op_arr.append(i)
        else:
            ele = op_arr[len(op_arr) - 1] + i
            op_arr.append(ele)
        
    print(op_arr)
    
    return op_arr

prefix_sum([1,2,3,4,5])


#### Alternate approach with validations

def prefix_sum(arr):
    if not hasattr(arr, '__iter__'):
        raise TypeError("Input must be an iterable of numbers")

    op_arr = []
    total = 0

    for num in arr:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numeric")
        total += num
        op_arr.append(total)

    print(op_arr)
    return op_arr

prefix_sum([1,"2",3,4,5])

