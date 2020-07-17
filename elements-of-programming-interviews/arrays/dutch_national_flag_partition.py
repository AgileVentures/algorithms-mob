#Write a program that takes an array A and an index i rnto A, 
#and rearranges the elements such that all elements less than A[r] (the "pivot") appear first, 
# followed by elements equal to the pivot, followed by elements greater than the pivot.

"""
    Can be solved by O(n) additional space by iterating throough the list
    Storing values that are less than the pivot in one array, values equal
    to the pivot in another and values less than the pivot in another
    Then later merging them in the correct order. Time complexity is O(n)

    *****

    We can improve the O(n) space to O(1) by doing two iterations, the 
    first one iterates all the elements starting from index 0 --> len(arr)
    moving them to a sub array of smaller elements, that are less than the pivot to the begining of the array,
    The second stage is similar to the first, difference is we now move elements larger
    than the pivot to the end of the array. 

"""


def dutch_national_flag_partition(arr, idx):
    pivot = arr[idx]
    swap_here = current_index = 0
    while current_index < len(arr):
        if arr[current_index] < pivot:
            if arr[swap_here] > pivot:
                swap_here += 1
                continue
            arr[current_index], arr[swap_here] =  arr[swap_here], arr[current_index]
            swap_here += 1
        current_index += 1
    current_index = swap_here
    swap_here = len(arr) - 1
    while current_index < swap_here:
        if arr[current_index] > pivot:
            if arr[swap_here] > pivot:
                swap_here -= 1
                continue
            arr[current_index], arr[swap_here] =  arr[swap_here], arr[current_index]
            swap_here -= 1
        current_index += 1
    return arr


print(dutch_national_flag_partition([0,2,1,2,2,0,0,0,1,2,1], 2))
print(dutch_national_flag_partition([0,2,1,2,2,2,0,0,1,2,0,0,1,2], 2))
print(dutch_national_flag_partition([0,2,1,2,2,0,0,0,0], 2))
print(dutch_national_flag_partition([0,1,1,2,2,1,0,0,1], 2))


 
