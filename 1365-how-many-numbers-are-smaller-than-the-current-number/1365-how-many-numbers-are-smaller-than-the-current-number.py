class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        occurences= {}
        for i in nums:
            if i in occurences:
                occurences[i]=occurences[i]+1
            else:
                occurences[i]=1
        uniqueOrdered = list(set(nums))
        uniqueOrdered.sort()
        noSmaller={}
        for x,i in enumerate(uniqueOrdered):
            _sum =0
            for y in uniqueOrdered[:x]:
                _sum+=occurences[y]
            noSmaller[i]=_sum
        return list(map(lambda i:noSmaller[i],nums))

