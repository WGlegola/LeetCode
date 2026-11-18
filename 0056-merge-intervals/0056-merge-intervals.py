class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key=lambda x:x[0])
        start = intervals[0][0]
        stop = intervals[0][1]
        solution = []
        newList=False
        for i in intervals[1:]:
            if i[0]>stop:
                solution.append([start,stop])
                newList=True
            else:
                if stop<i[1]:
                    stop=i[1]
            if newList:
                newList=False
                start=i[0]
                stop=i[1]
        solution.append([start,stop])
        return solution
                