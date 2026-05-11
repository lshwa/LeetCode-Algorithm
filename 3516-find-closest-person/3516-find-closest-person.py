class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        pos0 = abs(x - z)
        pos1 = abs(y - z)

        if pos0 < pos1:
            return 1
        
        elif pos1 < pos0:
            return 2
        
        else:
            return 0
        