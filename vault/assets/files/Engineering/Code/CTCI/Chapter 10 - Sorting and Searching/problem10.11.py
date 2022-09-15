# heap used just to simplify code
# at the expense of introducing larger constant/overhead
# Inplace algo
import heapq


def wiggleSort(nums: list[int]) -> None:
    i = 1
    nums.append(-float("inf"))
    while i < len(nums) - 1:
        h = [(-nums[i - 1], i - 1), (-nums[i], i), (-nums[i + 1], i + 1)]
        heapq.heapify(h)
        _, idx = heapq.heappop(h)
        nums[i], nums[idx] = nums[idx], nums[i]
        i += 2
    nums.pop()
