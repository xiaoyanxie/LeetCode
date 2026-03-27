class MedianFinder:

    def __init__(self):
        """
        1,2
        idx = 2
        stream[0] + stream
        123if a number is smaller than minh[0], add to maxh
        if a number is bigger than maxh[0],add to minh
        minh=[2]
        maxh=[1]
        """

        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        if not self.minh and not self.maxh:
            heapq.heappush(self.maxh, -num)
            
        elif num > (-self.maxh[0]):
            heapq.heappush(self.minh, num)

            if len(self.minh) - len(self.maxh) > 1:
                tmp = heapq.heappop(self.minh)
                heapq.heappush(self.maxh, -tmp)
               
        else:
            heapq.heappush(self.maxh, -num)

            if len(self.maxh) - len(self.minh) > 1:
                tmp = heapq.heappop(self.maxh)
                heapq.heappush(self.minh, -tmp)
                
    
    def findMedian(self) -> float:
        if len(self.minh) == len(self.maxh):
            return (self.minh[0] - self.maxh[0]) / 2
        elif len(self.minh) > len(self.maxh):
        
            return self.minh[0]
        else:
            return -self.maxh[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
