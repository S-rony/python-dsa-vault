def find_min_max(arr, start, end):
    if start == end:
        return arr[start], arr[end]
    if start + 1 == end:
        if arr[start] < arr[end]:
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]

    mid = (start+end) // 2
    min_1 , max_1 = find_min_max(arr, start, mid)
    min_2, max_2 = find_min_max(arr, mid+1, end)
    return min(min_1,min_2) , max(max_1, max_2)

arr = [23,14,45,3,6,10]
min, max = find_min_max(arr, 0, len(arr)- 1)
print("minimum", min)
print("maximum", max)
