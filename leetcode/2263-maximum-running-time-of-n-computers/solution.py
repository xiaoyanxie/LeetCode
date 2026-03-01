class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        # batteries.sort()

        minTime = 0
        maxTime = sum(batteries) // n

        def canRun(expectedTime):
            totalBatteryTime = 0
            for batteryTime in batteries:
                totalBatteryTime += min(expectedTime, batteryTime)
            return totalBatteryTime >= expectedTime * n

        found = -1
        while minTime <= maxTime:
            midTime = minTime + (maxTime - minTime) // 2
            if canRun(midTime):
                found = midTime
                minTime = midTime + 1
            else:
                maxTime = midTime - 1
        return found
