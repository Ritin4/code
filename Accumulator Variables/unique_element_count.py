def unique_element_count(arr):

    ele_count ={}

    for ele in arr:
        if ele not in ele_count:
            ele_count[ele] = 1
        else:
            ele_count[ele] += 1
    
    print(ele_count)

    return ele_count

unique_element_count([1,2,2,3,3,3,4,5,5,66])
