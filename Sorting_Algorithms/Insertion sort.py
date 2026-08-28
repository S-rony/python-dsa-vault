def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

a = [3,7,4,2,1,8]
insertion_sort(a)
print(a)

#
# for j in range(i - 1, 0 - 1, -1):
#     if key < arr[j]:
#         arr[j + 1] = arr[j]
#     else:
#         break
# else:
#     arr[0] = key