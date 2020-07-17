# Write a program which takes as input an array of digits encoding a nonnegative decimal integer D 
# and updates the array to represent the integer D + 1.
# For example, if the input is (1,2,9) then you should update the array to (1,3,0).
# Your algorithm should work even if it is implemented in a language that has finite-precision arithmetic.

def increment_integer(arr):
    quitiont, idx = 0, len(arr) - 1

    while idx >=  0:
        remainder = 0
        current_sum = remainder + arr[idx] + 1
        quotient = current_sum / 10
        remainder = current_sum % 10
        arr[idx] = remainder
        idx -= 1
    if quotient > 0:
        arr = [quotient] + arr
    return arr

print(increment_integer([1,2,3]))

