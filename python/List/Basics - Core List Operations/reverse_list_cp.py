'''
Problem: Given list of n integers, reverse in place 
Input: list of integers
Output: reversed list
'''
import time

def reverse_list_cp(arr):
    i , j = 0 , len(arr)-1                  #Assignment O(1)

    while i < j:                            
        arr[i] , arr[j] = arr[j], arr[i]
        i+=1
        j-=1

    return arr

def test(n):
    arr = list(range(n))
    start = time.perf_counter()
    reverse_list_cp(arr)
    end = time.perf_counter()

    return start - end

sizes = [10_000, 100_000, 1_000_000, 10_000_000]

for n in sizes:
    print(f"n={n:<10} time={test(n):.6f} seconds")