# Finding the Right_side leader
#brute_force O(n²)
arr = [16, 17, 4, 3, 5, 2]
arr_1 = []
arr_2 = []

for i in range(len(arr) ):
    is_leader = True
    for j in range(i+1, len(arr)):
        if arr[i] < arr[j]:
            is_leader = False
            break
    if is_leader:
        arr_1.append(arr[i])

print(arr_1)

#optimal solution Time: O(n) Space: O(1)


#transverse right to left

max = arr[len(arr)-1]
for k in range(len(arr) - 1, -1, -1):
    if max <= arr[k]:
        max = arr[k]
        arr_2.append(max)
arr_2.reverse()
print(arr_2)
