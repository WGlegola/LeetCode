class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        st = nums[0]
        by = 1
        for i in nums[1:]:
            if st == i:
                by += 1
            else:
                if by == 0:
                    by = 1
                    st = i
                else:
                    by -= 1
        return st
