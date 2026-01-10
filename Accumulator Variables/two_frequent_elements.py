#Find the two elements that appear the most number of times in an array.

def two_frequent_elements(arr):
    frequency_list = {}

    for ele in arr:
        if ele not in frequency_list:
            frequency_list[ele] = 1
        else:
            frequency_list[ele] += 1

    first_ele = None
    second_ele = None
    first_max = 0
    second_max = 0

    for ele, count in frequency_list.items():
        if count > first_max:
            second_ele = first_ele
            second_max = first_max

            first_ele = ele
            first_max = count

        elif count > second_max:
             second_ele = ele
             second_max = count 
    
    print("freq_list: ", frequency_list)
    print("first ele: ", first_ele)
    print("first_max: ", first_max)
    print("second_ele: ", second_ele)
    print("second_max: ", second_max)
    

# two_frequent_elements([1,2,1,2,2,3,4,4,5])
two_frequent_elements([1, 1, 1, 1, 4])



    
        
