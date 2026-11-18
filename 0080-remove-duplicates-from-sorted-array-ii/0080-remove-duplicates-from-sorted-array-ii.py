class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        skip = 0
        what = -1
        occurcence = 0
        for no, i in enumerate(nums):
            if what == i:
                occurcence += 1
            else:
                if occurcence > 2:
                    skip += occurcence - 2
                occurcence = 1
                what = i
            nums[no - skip] = nums[no]
        if occurcence > 2:
            skip += occurcence - 2
        return len(nums)-skip
