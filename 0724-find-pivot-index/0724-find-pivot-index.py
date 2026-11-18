class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum=0
        rightSum= sum(nums)
        for idi, i in enumerate(nums):
            rightSum -= i
            if leftSum == rightSum:
                return idi
            leftSum += i
        return -1
        