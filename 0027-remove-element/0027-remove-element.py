class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in reversed(range(len(nums))):
            if nums[i] == val:
                tmp = nums[i] 
                nums[i] = nums[-1-k]
                nums[-1-k]=tmp
                k += 1

        return len(nums)-k
