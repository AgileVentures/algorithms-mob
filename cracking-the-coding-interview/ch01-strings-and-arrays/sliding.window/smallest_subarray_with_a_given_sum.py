# Given an array a and an integer s, find the smallest sub array with sum greater than or equal to s


# example
#   input [4,2,2,7,8,1,2,8,1,0], 8 output: 1

def smallest_subarray_with_a_given_sum(arr, s):
    start_index = 0
    min_size = len(arr)
    current_sum = 0

    for i, j in enumerate(arr):
        current_sum += j

        while current_sum >= s:
            min_size = min(min_size, i - start_index + 1)
            current_sum -= arr[start_index]
            start_index += 1
        if min_size == 1:
            break
    return min_size    


print(smallest_subarray_with_a_given_sum([4,2,2,7,8,1,2,8,1,0], 8))


