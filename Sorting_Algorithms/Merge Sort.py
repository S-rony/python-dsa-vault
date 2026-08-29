def divide(arr, l , r):
    if l < r:
        m = (l+r)//2
        divide(arr, l , m)
        divide(arr, m+1, r)
        # divide(arr, l, m-1) correct
        # divide(arr, m , r) this we can do that as well
        merge(arr, l , m , r)


def merge(arr, l , m , r):
    s1 = m - l + 1
    # s2 = r - (m+1) + 1
    s2 = r - m

    left_arr = [0] * s1
    right_arr = [0] * s2

    for i in range(s1):
        left_arr[i] = arr[l+i]

    for j in range(s2):
        right_arr[j] = arr[m+1 + j]

    i = j = 0
    k = l

    while i < s1 and j < s2:
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i = i + 1
            k = k +1
        else:
            arr[k] = right_arr[j]
            j = j + 1
            k = k + 1

    while i < s1:
        arr[k] = left_arr[i]
        i = i + 1
        k = k +1

    while j < s2:
        arr[k] = right_arr[j]
        j = j +1
        k = k +1

arr = [21,34,11,5,45,9,50]
divide(arr,0, len(arr) - 1)
print(arr)












