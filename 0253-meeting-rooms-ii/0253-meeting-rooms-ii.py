class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = list(sorted(intervals,key= lambda x:x[0]))
        rooms = []
        for i in sorted_intervals:
            if len(rooms) == 0:
                rooms.append(i)
            else:
                added = False
                min_separation = float("inf")
                min_separation_pos = 0
                for idy, y in enumerate(rooms):
                    if y[1] > i[0]:
                        continue
                    else:
                        if min_separation > y[1]-i[0]:
                            min_separation = y[1]-i[0]
                            min_separation_pos = idy
                            added = True
                if added:
                    rooms[min_separation_pos][1]=i[1]
                else:
                    rooms.append(i)
        return len(rooms)
                    
                
        