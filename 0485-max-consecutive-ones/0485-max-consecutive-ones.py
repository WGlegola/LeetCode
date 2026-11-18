class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        consec = 0 if nums[0]==0 else 1
        maxConsec =consec
        for i in nums[1:]:
            if i==1:
                consec+=1
                continue
            if consec > maxConsec:
                maxConsec = consec
            consec = 0
        if consec > maxConsec:
            maxConsec = consec

        return maxConsec
