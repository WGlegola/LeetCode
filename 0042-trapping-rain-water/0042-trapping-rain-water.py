class Solution:
    def trap(self, height: List[int]) -> int:
        maxLList =[]
        maxRList =[]
        maxL = 0
        maxR = 0
        for i in height:
            if i > maxL:
                maxL = i
            maxLList.append(maxL)
            
        for i in reversed(height):
            if i > maxR:
                maxR = i
            maxRList.insert(0, maxR)
        water = 0
        for i in range(len(height)):
            water += min(maxLList[i],maxRList[i])-height[i]
                         
        return water
            
            
            