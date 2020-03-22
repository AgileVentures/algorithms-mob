# given an array a and an integer k, find the maximum sum of any of its sub-arrays of size k

# example
#   input [4,2,1,7,8,1,2,8,1,0], 3 output: 16


def maximum_sum_subarray(a, k):
    start_idex = 0
    end_idex = k - 1
    current_sum = 0
    max_sum = 0

    for i, j in enumerate(a):
        current_sum += j
        if i > end_idex:
            print(j)
            current_sum -= a[start_idex]
            start_idex += 1
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

print(maximum_sum_subarray([4,2,1,7,8,1,2,8,1,0], 3))