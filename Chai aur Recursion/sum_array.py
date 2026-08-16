#loop_approach
def sum_iterative(arr):
    total = 0
    for n in arr:
        total += n

    return total

#recursive_approach
def sum_recursive(arr):
     if not arr:
         return 0
     else:
         return arr[1] + sum_iterative(arr[1:])

