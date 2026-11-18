class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last = 0
        for i in nums:
            if i == nums[last]:
                continue
            last+=1
            nums[last]=i
        if nums[last] != nums[-1]:
            last+=1
            nums[last] = nums[-1]
        return last+1         
