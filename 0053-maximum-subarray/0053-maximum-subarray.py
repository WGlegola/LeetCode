class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum = float("-inf")
        curr= maxSum
        for i in range(len(nums)):
            if nums[i] > curr + nums[i]:
                curr = nums[i]
            else:
                curr += nums[i]
            if curr > maxSum:
                maxSum = curr
                
        return maxSum
            
            