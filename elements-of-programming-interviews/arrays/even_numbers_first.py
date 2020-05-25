# Your input is an array of integers, 
# and you have to reorder its entries so that the even entries appear first
# Space complexity of o(1) and o(n) time

#def reorder_even_to_appear_first(arr: List[int])-> List[int]:
def reorder_even_to_appear_first(arr):
    next_even, next_odd = 0, len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1
    return arr

print(reorder_even_to_appear_first([1,2,3,3,4,17,2]))
