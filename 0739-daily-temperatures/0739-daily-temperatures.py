class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        tempStack=[]
        anwser = temperatures[:]
        for tempNDay in enumerate(temperatures):
            while tempStack and tempStack[-1][1]<tempNDay[1]:
                temp = tempStack.pop()
                anwser[temp[0]]=tempNDay[0]-temp[0]
            tempStack.append(tempNDay)
        while tempStack:
            temp = tempStack.pop()
            anwser[temp[0]]=0
        return anwser
