class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m + n)[::-1]:
            if n==0:
                nums1[i] = nums1[m-1]
                m -= 1
            elif m==0:
                nums1[i] = nums2[n-1]
                n -= 1
            elif nums1[m-1] > nums2[n-1]:
                nums1[i] = nums1[m-1]
                m -= 1
            else:
                nums1[i] = nums2[n-1]
                n -= 1