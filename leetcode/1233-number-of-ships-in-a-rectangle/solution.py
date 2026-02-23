# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x0, y0, x1, y1 = bottomLeft.x, bottomLeft.y, topRight.x, topRight.y
        dx, dy = x1 - x0, y1 - y0
        if x0 > x1 or y0 > y1:
            return 0
        hasShips = sea.hasShips(topRight, bottomLeft)
        # print(f'checking ({x0},{y0}) -> ({x1},{y1}) = {hasShips}')
        if not hasShips:
            return 0
        
        if dx == 0 and dy == 0:
            return 1
        # divide and conquer
        """
        y1        .     .

      yMid        .     .
        
        y0
        . x0    xMid    x1
        """
        cnt = 0
        xMid, yMid = x0 + (x1 - x0) // 2, y0 + (y1 - y0) // 2
        # p(x0, y0) -> p(x2, y2)
        cnt += self.countShips(sea, Point(xMid, yMid), Point(x0, y0))
        # p(x0, y2) -> p(x2, y1)
        cnt += self.countShips(sea, Point(xMid, y1), Point(x0, yMid + 1))
        # p(x2, y0) -> p(x1, y2)
        cnt += self.countShips(sea, Point(x1, yMid), Point(xMid + 1, y0))
        # p(x2, y2) -> p(x1, y1)
        cnt += self.countShips(sea, Point(x1, y1), Point(xMid + 1, yMid + 1))
        return cnt
