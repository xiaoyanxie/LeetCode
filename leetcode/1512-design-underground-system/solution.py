from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        # check in: which station, what time

        """
        id -> (station, t)
        self.checkIn
        
        (station1, station2) -> (totalTime, #customers)
        self.avg
        """
        self.checkInRecord = defaultdict(Tuple[str, int])
        self.stat = defaultdict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # A customer with a card ID equal to id, checks in at the station stationName at time t.
        # A customer can only be checked into one place at a time.
        if id in self.checkInRecord:
            raise Exception(f'Customer {id} can only be checked into one place at a time.')
        self.checkInRecord[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # A customer with a card ID equal to id, checks out from the station stationName at time t.
        stationIn, t0 = self.checkInRecord.pop(id)
        
        record = (stationIn, stationName)
        if record not in self.stat:
            self.stat[record] = [0, 0]
        
        self.stat[record][0] += t - t0
        self.stat[record][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, numCustomers = self.stat[(startStation, endStation)]
        return totalTime / numCustomers


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
