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
        """
        y1         xm|      x1
        ym + 1       |      ym + 1
        ----------------------
        ym           |      ym
                     |
                     |
        y0           |
          x0       xm|xm+1  x1

        xm = x0 + (x1 - x0) // 2
        ym = y0 + (y1 - y0) // 2

        from (x0, y0) to (xm, ym)
        from (xm + 1, y0) to (x1, ym)
        from (x0, ym + 1) to (xm, y1)
        from (xm + 1, ym + 1) to (x1, y1)
        """
        x0, y0 = bottomLeft.x, bottomLeft.y
        x1, y1 = topRight.x, topRight.y

        if x0 > x1 or y0 > y1:
            return 0
        
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        if x0 == x1 and y0 == y1:
            return 1
        
        xm = x0 + (x1 - x0) // 2
        ym = y0 + (y1 - y0) // 2

        return (self.countShips(sea, Point(xm, ym), Point(x0, y0))
             + self.countShips(sea, Point(x1, ym), Point(xm + 1, y0))
             + self.countShips(sea, Point(xm, y1), Point(x0, ym + 1))
             + self.countShips(sea, Point(x1, y1), Point(xm + 1, ym + 1)))
