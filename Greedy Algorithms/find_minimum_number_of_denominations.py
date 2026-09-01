def min_number_deno(arr, amount):
    arr.sort()
    n = len(arr)
    j = n - 1
    count = 0
    for i in range(j,-1,-1):
        while amount >= arr[i]:
            amount = amount - arr[i]
            count += 1
    return count
arr = [1,2,5,10,20,50,100,500]
amount = int(input("Enter amount: "))
c = min_number_deno(arr, amount)
print(c)

