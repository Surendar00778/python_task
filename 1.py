def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def kth_smallest(arr, low, high, k):
    if k > 0 and k <= (high - low + 1):
        pivot_index = partition(arr, low, high)

        if pivot_index - low == k - 1:
            return arr[pivot_index]

        if pivot_index - low > k - 1:
            return kth_smallest(arr, low, pivot_index - 1, k)

        return kth_smallest(arr, pivot_index + 1, high, k - pivot_index + low - 1)

    return None

# Example usage:
arr1 = [10, 3, 6, 9, 2, 4, 15, 23]
k1 = 4
result1 = kth_smallest(arr1, 0, len(arr1) - 1, k1)
print(f"Kth smallest element for k={k1} is {result1}")

arr2 = [5, -8, 10, 37, 101, 2, 9]
k2 = 6
result2 = kth_smallest(arr2, 0, len(arr2) - 1, k2)
print(f"Kth smallest element for k={k2} is {result2}")
