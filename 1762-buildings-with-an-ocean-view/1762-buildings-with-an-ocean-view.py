class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = -1
        answ = []
        for idx, i in enumerate(heights[::-1]):
            if i > max_height:
                answ.append(len(heights)-idx-1)
                max_height = i
        return answ[::-1]