def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modifies nums1 in-place instead.
    """
    i, j = m - 1, n - 1
    pos = m + n - 1
    while i >= -1 and j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[pos] = nums1[i]
            i -= 1
        else:
            nums1[pos] = nums2[j]
            j -= 1
        pos -= 1
