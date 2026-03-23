def quick_sort(arr, L, R):
    if L >= R:
        return arr
    
    pivot_val = arr[R]
    pivot_index = L # Pointing to the first value that is greater than the pivot

    for i in range(L, R):
        if arr[i] < pivot_val:
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            pivot_index += 1
    
    # DONT forget this - This moves the pivot element into the correct position
    # Then we dont have to worry about sorting this element anymore, so we can just sort:
    # (L, pivot_index - 1) and (pivot_index + 1, R)
    arr[pivot_index], arr[R] = arr[R], arr[pivot_index]

    quick_sort(arr, L, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, R)

    return arr

arr = [1, 1, 4, 6, 1, 3]
L, R =  0, len(arr) - 1
print(quick_sort(arr, L, R))
