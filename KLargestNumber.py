def partition(arr):
    pivot = arr[-1]
    j = 0
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[-1] = arr[-1], arr[j]
    return arr


def partition_rev(arr):
    pivot = arr[-1]
    j = 0
    for i in range(len(arr) - 1):
        if arr[i] >= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[-1] = arr[-1], arr[j]
    return arr


def find_kth_largest(nums, k):
    lo = 0
    hi = j = len(nums)
    currk = len(nums) + 1

    while k != currk:
        pivot = nums[hi - 1]
        j = lo
        for i in range(lo, hi - 1):
            if nums[i] >= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[j], nums[hi - 1] = nums[hi - 1], nums[j]
        currk = j + 1  # add 1 to get k position because j is zero-based array
        if k < currk:
            hi = j
        if k > currk:
            lo = j + 1

    return nums[j]


# print(partition([5, 6, 2, 3, 1, 4]))
# print(partition_rev([3, 2, 1, 5, 6, 4]))

assert find_kth_largest([3, 2, 1, 5, 6, 4], 1) == 6
assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
assert find_kth_largest([3, 2, 1, 5, 6, 4], 3) == 4
assert find_kth_largest([3, 2, 1, 5, 6, 4], 4) == 3
assert find_kth_largest([3, 2, 1, 5, 6, 4], 5) == 2
assert find_kth_largest([3, 2, 1, 5, 6, 4], 6) == 1

arr1 = [i for i in range(1000000)]
# print(find_kth_largest(arr1, 1))
