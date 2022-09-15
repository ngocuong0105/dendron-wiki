from random import randint

nums = [3,5,2,4,6,1]
def random_partition(l,r):
    idx = randint(l,r)
    idx = l
    nums[r],nums[idx] = nums[idx],nums[r]
    pivot = nums[r]
    i = l-1
    for j in range(l,r):
        if nums[j] > pivot:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
    nums[i+1],nums[r] = nums[r],nums[i+1]
    return i+1

def kth(l,r,k):
    if l == r: return nums[l]
    q = random_partition(l,r)
    i = q-l+1 # very important line = indecing in l,r array
    if k == i: return nums[q]
    elif k<i: return kth(l,q-1,k)
    else: return kth(q+1,r,k-i)
