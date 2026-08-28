def selection_sort(a):
    n = len(a)

    for i in range(n):
        min_index = i                               #first loop iteration is the minimum
        for j in range(i,n):
            if a[j] < a[min_index]:
                min_index = j
        a[i],a[min_index] = a[min_index],a[i]

a = [3,7,4,2,1,8]
selection_sort(a)
print(a)
