class Solution:
    grid = 0
    
    def removeIsland(self,i,j):
        if self.grid[i][j] == "0":
            return
        else:
            self.grid[i][j] = "0"
            if i>0:
                self.removeIsland(i-1,j)

            if i<len(self.grid)-1:
                self.removeIsland(i+1,j)

            if j>0:
                self.removeIsland(i,j-1)

            if j<len(self.grid[0])-1:
                self.removeIsland(i,j+1)
                
    def numIslands(self, grid: List[List[str]]) -> int:
        noIslands = 0
        self.grid = grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "1":
                    noIslands+=1
                    self.removeIsland(i,j)
        return noIslands
        
                    
                    
   