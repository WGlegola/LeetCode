class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        existing = set()
        culprit =0
        for i in nums:
            if i in existing:
                culprit = i
                break
            existing.add(i)
        print(len(nums))
        print(culprit)

        missing = set(range(1, len(nums)+1)) - set(nums)
        return [culprit,missing.pop()]