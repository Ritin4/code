#Find the two elements that appear the most number of times in an array.

def two_frequent_elements(arr):
    # Count frequencies
    frequency = {}

    for x in arr:
        if x not in frequency:
            frequency[x] = 1
        else:
            frequency[x] += 1

    # Track top two frequencies
    first_element = None
    second_element = None
    first_count = 0
    second_count = 0

    # Evaluate each element's frequency
    for element, count in frequency.items():
        if count > first_count:
            # Shift current first into second
            second_element = first_element
            second_count = first_count

            # Update first
            first_element = element
            first_count = count

        elif count > second_count:
            second_element = element
            second_count = count

    print("first_element", first_element)
    print("second_element", second_element)


    return first_element, second_element
    

# two_frequent_elements([1,2,1,2,2,3,4,4,5])
two_frequent_elements([1, 1, 1, 1, 5])



    
        
