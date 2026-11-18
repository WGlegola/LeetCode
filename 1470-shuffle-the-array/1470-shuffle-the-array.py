class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n]
        nums2 = nums[n:]
        ans=[]
        for i in range(n):
            ans+=[nums1[i]]+[nums2[i]]
        return ans
