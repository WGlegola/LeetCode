class SparseVector:
    def __init__(self, nums: list):
        self.positions = []
        self.values = []
        for idx, i in enumerate(nums):
            if i != 0:
                self.positions.append(idx)
                self.values.append(i)
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum_of_dot = 0
        for pos,value in zip(self.positions,self.values):
            if pos in vec.positions:
                sum_of_dot += value * vec.values[vec.positions.index(pos)]
        return sum_of_dot
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)