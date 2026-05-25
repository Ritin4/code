def primeChecker(arr):
    for num in arr:
        if num == 2:
            print(num)
            return num
        
        if num <2 or num % 2 == 0:
            continue
        
        for i in range(3, num):
            if num % 3 == 0:
                continue
            print(num)
            return num
    return

primeChecker([1,9,12,7,10,11,15,20,2])