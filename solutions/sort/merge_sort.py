# Implementation of MergeSort

# Why pass these in as params?
#  - In many languages (like Python), slicing creates a copy of the data.
#  - 
def merge_sort(arr, L, R):
    if R == L:
        return [arr[R]]
    
    mid = (L + R) // 2

    left_subarray = merge_sort(arr, L, mid)
    right_subarray = merge_sort(arr, mid + 1, R)

    return merge(left_subarray, right_subarray)

def merge(left_arr, right_arr):
    l_index = 0
    r_index = 0

    result = []

    while l_index < len(left_arr) and r_index < len(right_arr):
        if left_arr[l_index] <= right_arr[r_index]:
            result.append(left_arr[l_index])
            l_index += 1
        else:
            result.append(right_arr[r_index])
            r_index += 1
        
    if l_index == len(left_arr):
        result += right_arr[r_index:]
    else:
        result += left_arr[l_index:]
    
    return result

arr = [9, 20, 5, 2, 4, 6, 1, 3, 7, 8, 0, 30, -1, -20]
L, R = 0, len(arr) - 1

print(merge_sort(arr, L, R))
