class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aPointer=0
        bPointer=0
        for i in nums:
            
            bPointer=aPointer+1
            for j in nums[aPointer+1:]:
                if i + j == target:
                    return [aPointer, bPointer]
                bPointer+=1
            aPointer+=1
        