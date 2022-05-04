class SortArray:
    def sort(arr):
        low = 0
        mid = 0
        high = a.length - 1
        while mid <= high:
            if a[mid] == 0:
                temp = arr[low]
                arr[low] = arr[mid]
                arr[mid] = temp
                # Swap(arr,arr[low],arr[mid])
                low += 1
                high += 1
            if a[mid] == 1:
                mid += 1
            if a[mid] == 2:
                temp = arr[mid]
                arr[mid] = arr[high]
                arr[high] = temp
                high -= 1








