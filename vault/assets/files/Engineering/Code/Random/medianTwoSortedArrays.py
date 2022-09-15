class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        print(self.kth(A, B, l // 2))
        return (self.kth(A, B, l // 2) + self.kth(A, B, (l - 1) // 2)) / 2

    def kth(self, A, B, k):
        if len(A) == 0:
            return B[k]
        if len(B) == 0:
            return A[k]
        i, j = len(A) // 2, len(B) // 2
        if i + j >= k:
            if A[i] > B[j]:
                return self.kth(A[:i], B, k)
            else:
                return self.kth(A, B[:j], k)
        else:
            if A[i] > B[j]:
                return self.kth(A, B[j + 1 :], k - j - 1)
            else:
                return self.kth(A[i + 1 :], B, k - i - 1)
