def quick_sort(arr, l, r):
    # Jab tak left index, right index se chhota hai
    if l < r:
        # Partition function ko call karke pivot ka sahi index (p) nikalenge
        p = partition(arr, l, r)

        # Left wale hisse ko sort karne ke liye recursive call
        quick_sort(arr, l, p - 1)

        # Right wale hisse ko sort karne ke liye recursive call
        quick_sort(arr, p + 1, r)


def partition(arr, l, r):
    pivot = arr[l]  # Pehle element ko pivot maan liya
    i = l + 1  # Left side ka pointer
    j = r  # Right side ka pointer

    while True:  # Infinite loop jo break hone tak chalega

        # Left se chote elements ko skip karte jao
        while i <= j and arr[i] < pivot:
            i += 1

        # Right se bade elements ko skip karte jao
        while i <= j and arr[j] > pivot:
            j -= 1

        # Agar dono pointers cross nahi huye hain, toh elements ko swap karo
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            # Agar i aur j cross ho gaye hain (ya barabar ho gaye hain), toh loop tod do
            break

    # Loop tootne ke baad Pivot ko uski sahi jagah (j index) par swap kar do
    arr[l], arr[j] = arr[j], arr[l]

    # Pivot ka naya index return kar do
    return j


# --- Video ke end mein run kiya gaya actual Test Array ---
arr = [23, 45, 12, 65, 34, 10, 3]

# QuickSort ko call kiya (starting index 0 se end index len-1 tak)
quick_sort(arr, 0, len(arr) - 1)

# Sorted array ko print karaya
print(arr)