RED, WHITE, BLACK = range(3)

def dutch_flag_partition(p, arr):
    pivot = arr[p] 
    # first pass group elements smaller than the pivot
    smaller = 0

    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
    larger = len(arr) - 1
    # second pass group elements larger than the pivot
    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            break
        elif arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1
    return arr
print(dutch_flag_partition(2, [2,0,1,2,2,2,1,1,1,0,0,0,2]))

