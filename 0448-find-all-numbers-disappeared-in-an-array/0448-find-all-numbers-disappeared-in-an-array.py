class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        unique = set(nums)
        fullSet = set(range(1,len(nums)+1))
        return list(fullSet-unique)