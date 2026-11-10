def rotated_index(values, target):
    lo, hi = (0, len(values) - 1)
    while lo <= hi:
        mid = (lo + hi) // 2
        if values[mid] == target:
            return mid
        if values[lo] <= values[mid]:
            if values[lo] <= target < values[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        elif values[mid] < target <= values[hi]:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
